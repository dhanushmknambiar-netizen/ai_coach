# agents/session_manager.py

class SessionManager:
    def __init__(self, memory):
        """
        memory: Memory instance (from memory/memory.py)
        This SessionManager stores resume index under key 'resume_index'
        and stores recent session summaries under key 'last_session_summary'.
        """
        self.memory = memory
        self.key = "resume_index"
        self.summary_key = "last_session_summary"

    def save_index(self, idx):
        self.memory.save(self.key, idx)

    def load_index(self):
        v = self.memory.load(self.key)
        if v is None:
            return 0
        try:
            return int(v)
        except:
            return 0

    def clear(self):
        self.memory.save(self.key, 0)

    # --- new session save/load helpers used by main.py ---
    def save_session(self, summary):
        """
        Save a simple session summary into memory (under summary_key).
        summary: string or dict
        """
        # store as-is; Memory implementation can be extended later to persist
        self.memory.save(self.summary_key, summary)
        return True

    def load_session(self):
        """
        Return last saved session summary or None
        """
        return self.memory.load(self.summary_key)

