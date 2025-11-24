# memory/memory.py
import json
import os
from typing import Any

class Memory:
    def __init__(self, filename="memory_store.json"):
        self.filename = filename
        self.data = {}
        self.sessions = {}
        self._load_from_disk()

    # --- disk persistence helpers ---
    def _load_from_disk(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    obj = json.load(f)
                    self.data = obj.get("data", {})
                    self.sessions = obj.get("sessions", {})
            except Exception:
                # if file corrupted, start fresh
                self.data = {}
                self.sessions = {}

    def _save_to_disk(self):
        payload = {"data": self.data, "sessions": self.sessions}
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)

    # --- simple key-value store ---
    def save(self, key: str, value: Any):
        self.data[key] = value
        self._save_to_disk()

    def load(self, key: str):
        return self.data.get(key, None)

    # --- session storage (for resume / summaries) ---
    def save_session(self, session_id: str, state_dict: dict):
        self.sessions[session_id] = state_dict
        self._save_to_disk()

    def load_session(self, session_id: str):
        return self.sessions.get(session_id, None)

    def delete_session(self, session_id: str):
        if session_id in self.sessions:
            del self.sessions[session_id]
            self._save_to_disk()
