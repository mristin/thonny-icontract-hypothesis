"""Test the plugin functions both public and private."""
import os
import sys
import unittest
import unittest.mock

import thonnycontrib.thonny_icontract_hypothesis


class TestEnabled(unittest.TestCase):
    def test_enabled_in_editor(self) -> None:
        editor = unittest.mock.Mock()
        # Return just something which is non-None
        editor.get_current_editor.return_value = unittest.mock.Mock()

        workbench = unittest.mock.Mock()
        workbench.get_editor_notebook.return_value = editor

        self.assertTrue(
            thonnycontrib.thonny_icontract_hypothesis._enabled(workbench=workbench))

    def test_disabled_without_editor(self) -> None:
        workbench = unittest.mock.Mock()
        workbench.get_editor_notebook.return_value.get_current_editor.return_value = \
            None

        self.assertFalse(
            thonnycontrib.thonny_icontract_hypothesis._enabled(workbench=workbench))


class TestTest(unittest.TestCase):
    def test_that_error_is_shown_without_editor(self) -> None:
        workbench = unittest.mock.Mock()
        workbench.get_editor_notebook.return_value.get_current_editor.return_value = None

        with unittest.mock.patch("tkinter.messagebox.showerror") as showerror:
            thonnycontrib.thonny_icontract_hypothesis._test(
                workbench=workbench,
                only_at=False
            )

            showerror.assert_called_with(
                title="No active editor",
                message=unittest.mock.ANY
            )

    def test_that_error_is_shown_without_filename(self) -> None:
        editor = unittest.mock.Mock()
        editor.get_filename.return_value = None

        workbench = unittest.mock.Mock()
        workbench.get_editor_notebook.return_value.get_current_editor.return_value = \
            editor

        with unittest.mock.patch("tkinter.messagebox.showerror") as showerror:
            thonnycontrib.thonny_icontract_hypothesis._test(
                workbench=workbench,
                only_at=False
            )

            showerror.assert_called_with(
                title="No file name",
                message=unittest.mock.ANY
            )

    def test_the_test_command(self) -> None:
        editor = unittest.mock.Mock()
        editor.get_filename.return_value = "some file.py"

        workbench = unittest.mock.Mock()
        workbench.get_editor_notebook.return_value.get_current_editor.return_value = \
            editor

        with unittest.mock.patch("thonny.get_shell") as get_shell:
            shell = unittest.mock.Mock()
            get_shell.return_value = shell

            thonnycontrib.thonny_icontract_hypothesis._test(
                workbench=workbench,
                only_at=False
            )

            editor.save_file.assert_called_once()

            shell.text.submit_command.assert_called_with(
                cmd_line=f'! {sys.executable} -m icontract_hypothesis test '
                         '-p "some file.py"\n',
                tags=unittest.mock.ANY
            )

    def test_the_test_at_command(self) -> None:
        editor = unittest.mock.Mock()
        editor.get_filename.return_value = "some file.py"
        editor.get_code_view.return_value.get_selected_range.return_value.lineno = 1984

        workbench = unittest.mock.Mock()
        workbench.get_editor_notebook.return_value.get_current_editor.return_value = \
            editor

        with unittest.mock.patch("thonny.get_shell") as get_shell:
            shell = unittest.mock.Mock()
            get_shell.return_value = shell

            thonnycontrib.thonny_icontract_hypothesis._test(
                workbench=workbench,
                only_at=True
            )

            editor.save_file.assert_called_once()

            shell.text.submit_command.assert_called_with(
                cmd_line=f'! {sys.executable} -m icontract_hypothesis test '
                         '-p "some file.py" --include 1984\n',
                tags=unittest.mock.ANY
            )


if __name__ == "__main__":
    unittest.main()
