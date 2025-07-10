# This is free and unencumbered software released into the public domain.

"""ASIMOV for LlamaIndex: Exception classes."""

from __future__ import annotations  # for Python 3.9


class AsimovModuleNotFound(Exception):
    """Exception raised when a module cannot be found or imported.

    Attributes:
        module_name: The name of the module that was not found
        message: Explanation of the error
    """

    def __init__(self, module_name: str, message: str | None = None) -> None:
        """Initializes the `AsimovModuleNotFound` exception.

        Args:
            module_name: The name of the module that was not found
            message: Optional custom error message. If not provided,
                    a default message will be generated.
        """
        self.module_name = module_name
        if message is None:
            message = f"Module '{module_name}' not found"
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        """Returns a string representation of the exception."""
        return self.message

    def __repr__(self) -> str:
        """Returns a detailed string representation of the exception."""
        return f"{self.__class__.__name__}(module_name={self.module_name!r}, message={self.message!r})"


class AsimovCommandError(Exception):
    """Exception raised when a subprocess command fails to execute properly.

    Attributes:
        command: The shell command that was run
        stderr: The error output from the command, if any
    """

    def __init__(self, command: str, stderr: str | None = None) -> None:
        """Initializes the `AsimovCommandError` exception.

        Args:
            command: The failed command
            stderr: Optional standard error output from the command
        """
        self.command = command
        self.stderr = stderr
        message = f"Command failed: {command}"
        if stderr:
            message += f"\nError output: {stderr}"
        super().__init__(message)

    def __str__(self) -> str:
        """Returns a string representation of the exception."""
        return super().__str__()


class AsimovJSONDecodeError(Exception):
    """Exception raised when JSON output cannot be decoded.

    Attributes:
        raw_output: The raw string output that failed decoding
        message: Explanation of the error
    """

    def __init__(self, raw_output: str, message: str | None = None) -> None:
        """Initializes the `AsimovJSONDecodeError` exception.

        Args:
            raw_output: The string that failed to decode
            message: Optional custom error message
        """
        self.raw_output = raw_output
        self.message = message or "Failed to decode JSON from ASIMOV output"
        super().__init__(self.message)

    def __str__(self) -> str:
        """Returns a string representation of the exception."""
        return self.message


class AsimovJsonLdError(Exception):
    """Exception raised when JSON-LD parsing or flattening fails.

    Attributes:
        detail: Optional string describing the parsing issue
    """

    def __init__(self, detail: str | None = None) -> None:
        """Initializes the `AsimovJsonLdError` exception.

        Args:
            detail: Optional detailed explanation of the JSON-LD error
        """
        self.detail = detail
        message = f"JSON-LD processing error{': ' + detail if detail else ''}"
        super().__init__(message)

    def __str__(self) -> str:
        """Returns a string representation of the exception."""
        return super().__str__()
