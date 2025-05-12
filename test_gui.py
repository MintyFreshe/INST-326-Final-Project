from gui import MainGui
import pytest
import tkinter as tk

@pytest.fixture
def gui_instance():
    root = tk.Tk()
    gui = MainGui()
    yield gui
    root.destroy()
    root.quit()

def test_gui_initialization(gui_instance):
    # Test if the GUI initializes with the correct title and dimensions
    assert gui_instance.root.title() == "My Budget App"
    assert gui_instance.root.geometry() == "1200x600"

def test_form_fields(gui_instance):
    # Test if all form fields are created correctly
    expected_fields = ['Name', 'Budget', 'Food', 'Transport', 'Housing', 'Entertainment', 'Savings', 'Miscellaneous']
    actual_fields = [field[0] for field in gui_instance.entries]
    assert actual_fields == expected_fields

def test_process_entry(gui_instance):
    # Test if the form processes entries correctly
    for field, entry in gui_instance.entries:
        entry.insert(0, "100")  # Simulate user input
    processed_data = gui_instance.process_entry()
    assert all(value == "100" for value in processed_data.values())

def test_on_submit(gui_instance):
    # Test if the submit button processes data correctly
    for field, entry in gui_instance.entries:
        entry.insert(0, "100")  # Simulate user input
    data = gui_instance.on_submit()
    assert data['Name'] == "100"  # Example check
    assert data['Budget'] == "100"

def test_create_charts(gui_instance):
    # Test if charts are created without errors
    gui_instance.create_charts()
    assert gui_instance.chart1_canvas is not None
    assert gui_instance.chart2_canvas is not None
    assert gui_instance.chart3_canvas is not None

def test_update_charts(gui_instance):
    # Test if charts update correctly with new data
    labels = ['Food', 'Transport', 'Housing']
    sizes = [100, 200, 300]
    gui_instance.update_charts(labels, sizes)
    assert gui_instance.chart_data['labels'] == labels
    assert gui_instance.chart_data['sizes'] == sizes

if __name__ == "__main__":
    pytest.main()



