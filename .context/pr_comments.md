# PR Review - Data backup and point-in-time recovery (by Meera)

## Reviewer: Amit Desai
---

**Overall:** Good foundation but critical bugs need fixing before merge.

### `backupManager.py`

> **Bug #1:** Incremental backup includes all records instead of only changed records since last backup
> This is the higher priority fix. Check the logic carefully and compare against the design doc.

### `recoveryEngine.py`

> **Bug #2:** Recovery point selection uses wrong comparison so it restores one snapshot too far
> This is more subtle but will cause issues in production. Make sure to add a test case for this.

---

**Meera**
> Acknowledged. I have documented the issues for whoever picks this up.
