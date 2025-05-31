# Codex Python SDK

This is a minimal Python wrapper for the `codex` command line tool.
It allows running Codex in *full‑auto* mode from Python scripts.

```
from codex_python import run_codex

result = run_codex("create a new file", working_dir="/path/to/repo")
print(result.stdout)
```

The SDK simply spawns the `codex` binary. Ensure the CLI is installed
and available on your `$PATH`.
