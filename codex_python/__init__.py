"""Minimal Python SDK for the Codex CLI.

This module provides a small wrapper around the ``codex`` command
line tool. It allows running Codex in full-auto mode and capturing the
output programmatically.
"""
from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Optional, Sequence

__all__ = ["CodexCLI", "run_codex"]


class CodexCLI:
    """Thin wrapper around the ``codex`` command line interface."""

    def __init__(
        self,
        codex_bin: str = "codex",
        working_dir: Optional[Path] = None,
        approval_mode: str = "full-auto",
        full_auto_error_mode: str | None = None,
        extra_args: Optional[Sequence[str]] = None,
    ) -> None:
        self.codex_bin = codex_bin
        self.working_dir = Path(working_dir) if working_dir else None
        self.approval_mode = approval_mode
        self.full_auto_error_mode = full_auto_error_mode
        self.extra_args = list(extra_args) if extra_args else []

    def run(self, prompt: str, *args: str) -> subprocess.CompletedProcess:
        """Run Codex with the given prompt.

        Any additional ``args`` are appended to the command.
        The process output is returned via ``subprocess.CompletedProcess``.
        """
        cmd: list[str] = [self.codex_bin]
        if self.approval_mode:
            cmd += ["--approval-mode", self.approval_mode]
        if self.full_auto_error_mode:
            cmd += ["--full-auto-error-mode", self.full_auto_error_mode]
        cmd += self.extra_args
        cmd += list(args)
        cmd.append(prompt)

        return subprocess.run(
            cmd,
            cwd=self.working_dir,
            text=True,
            capture_output=True,
            check=False,
        )


def run_codex(prompt: str, *args: str, **kwargs) -> subprocess.CompletedProcess:
    """Convenience function to run Codex in full-auto mode."""
    cli = CodexCLI(**kwargs)
    return cli.run(prompt, *args)
