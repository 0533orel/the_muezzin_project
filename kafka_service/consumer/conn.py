import json, threading, time
from collections import deque

from kafka import KafkaConsumer
from config import Config


class ConsumerManager:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self._consumer: KafkaConsumer = None
        self._thread: threading.Thread = None
        self._stop = threading.Event()
        self._paused = False
        self._buf = deque(maxlen=self.cfg.MAX_BUFFER)

    def start(self):
        self._consumer = KafkaConsumer(
            self.cfg.TOPIC,
            bootstrap_servers=self.cfg.BOOTSTRAP_SERVERS,
            group_id=self.cfg.GROUP_ID,
            auto_offset_reset=self.cfg.AUTO_OFFSET,
            enable_auto_commit=True,
            value_deserializer=lambda b: json.loads(b.decode("utf-8")),
        )
        self._stop.clear()
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def _loop(self):
        while not self._stop.is_set():
            if self._paused:
                time.sleep(0.1)
                continue
            try:
                for records in self._consumer.poll(timeout_ms=200).values():
                    for r in records:
                        print(r.value)
            except Exception as ex:
                print("[es-consumer] poll error:", ex)
                time.sleep(0.5)

    def stop(self):
        self._stop.set()
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=5)
        if self._consumer:
            try:
                self._consumer.close()
            except Exception:
                pass

    def pause(self): self._paused = True
    def resume(self): self._paused = False
    def clear(self): self._buf.clear()
    def get_messages(self, limit: int = 50):
        n = max(0, min(limit, len(self._buf)))
        return list(self._buf)[-n:]
