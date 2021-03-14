"""Automatically test Python code using icontract-hypothesis in Thonny."""
import subprocess
import tkinter.messagebox

import thonny
import thonny.workbench

name = "thonny-icontract-hypothesis"  # pylint: disable=invalid-name

# From: https://github.com/Franccisco/thonny-black-code-format/blob/master/thonnycontrib/thonny_black_format/__init__.py
# Temporary fix: this function comes from thonny.running, but importing that
# module may conflict with outdated Thonny installations from some Linux
# repositories.
_console_allocated = False  # pylint: disable=invalid-name


def _enabled(workbench: thonny.workbench.Workbench) -> bool:
    """Check whether the commands should be enabled."""
    editor = workbench.get_editor_notebook().get_current_editor()

    if editor is None:
        return False

    # Allow the user to run the command even if the file name has not been specified.
    # This will cause an error to be shown to the user, but also inform her that
    # the file needs to be saved.
    # Otherwise, the user is in the dark why the file can not be checked.
    return True


def _test(workbench: thonny.workbench.Workbench, only_at: bool) -> None:
    """
    Test the code with icontract-hypothesis.

    If ``only_at`` is True, test only the function under the caret.
    """
    editor = workbench.get_editor_notebook().get_current_editor()

    if editor is None:
        tkinter.messagebox.showerror(
            title="No active editor",
            message="No file is currently edited. "
            "Hence icontract-hypothesis test can not be performed.",
        )
        return

    filename = editor.get_filename()
    if filename is None:
        tkinter.messagebox.showerror(
            title="No file name",
            message="The current file has not been saved and does not have a name so "
            "it can not be tested with icontract-hypothesis. "
            "Please save the file first.",
        )
        return

    editor.save_file()

    cmd = ["!", "python", "-m", "icontract_hypothesis", "test", "-p", filename]
    if only_at:
        selection = editor.get_code_view().get_selected_range()
        cmd.extend(["--include", str(selection.lineno)])

    cmd_line = subprocess.list2cmdline(cmd)

    thonny.get_shell().text.submit_command(cmd_line=cmd_line + "\n", tags=("magic",))

    return


def _load_plugin(workbench: thonny.workbench.Workbench) -> None:
    """Add the plug-in commands to the workbench."""
    workbench.add_command(
        command_id="icontract_hypothesis.test",
        menu_name="tools",
        command_label="Test the current file with icontract-hypothesis",
        handler=lambda: _test(workbench=workbench, only_at=False),
        tester=lambda: _enabled(workbench=workbench),
    )

    workbench.add_command(
        command_id="icontract_hypothesis.test_at",
        menu_name="tools",
        command_label="Test the function under the caret with icontract-hypothesis",
        handler=lambda: _test(workbench=workbench, only_at=True),
        tester=lambda: _enabled(workbench=workbench),
    )


if thonny.get_workbench() is not None:
    _load_plugin(workbench=thonny.get_workbench())
