"""
Backup Manager — creates full and incremental backups of data.

This module is COMPLETE and WORKING. Your task is in recoveryEngine.py.

Author: Priya Menon (Data team)
Last Modified: 2026-03-25
"""

import hashlib
import json
import time
from typing import Dict, List, Optional
from datetime import datetime


class BackupSnapshot:
    def __init__(self, backup_id: str, data: Dict, change_log: List[Dict]):
        self.backup_id = backup_id
        self.timestamp = datetime.utcnow().isoformat()
        self.data = dict(data)
        self.change_log = list(change_log)
        self.checksum = self._compute_checksum()

    def _compute_checksum(self) -> str:
        content = json.dumps(self.data, sort_keys=True)
        return hashlib.sha256(content.encode()).hexdigest()


class BackupManager:
    def __init__(self):
        self.current_data: Dict = {}
        self.change_log: List[Dict] = []
        self.backups: List[BackupSnapshot] = []

    def set_data(self, key: str, value):
        """Set a value and record the change."""
        old_value = self.current_data.get(key)
        self.current_data[key] = value
        self.change_log.append({
            'timestamp': datetime.utcnow().isoformat(),
            'operation': 'set',
            'key': key,
            'old_value': old_value,
            'new_value': value,
        })

    def delete_data(self, key: str):
        """Delete a value and record the change."""
        old_value = self.current_data.pop(key, None)
        self.change_log.append({
            'timestamp': datetime.utcnow().isoformat(),
            'operation': 'delete',
            'key': key,
            'old_value': old_value,
            'new_value': None,
        })

    def create_backup(self, backup_id: str) -> BackupSnapshot:
        """Create a full backup snapshot."""
        snapshot = BackupSnapshot(backup_id, self.current_data, self.change_log)
        self.backups.append(snapshot)
        return snapshot

    def get_backup(self, backup_id: str) -> Optional[BackupSnapshot]:
        """Retrieve a backup by ID."""
        for b in self.backups:
            if b.backup_id == backup_id:
                return b
        return None

    def get_current_data(self) -> Dict:
        return dict(self.current_data)
