from funq.testcase import FunqTestCase

class AppTestCase(FunqTestCase):
    app_config_name = 'app_test'
    
    def start_dialog(self,btn_name):
        btn = self.funq.widget(path='mainWindow::QWidget::' + btn_name)
        btn.click()

    def get_status_text(self):
        return self.funq.widget(path='mainWindow::statusBar::QLabel').properties()['text']

class TestClick(AppTestCase):
    
    def test_simple_click(self):
        self.start_dialog('click')
        btn = self.funq.widget(path='mainWindow::ClickDialog::QPushButton')
        btn.click()
        self.assertEquals(self.get_status_text(), 'clicked !')
    
    def test_double_click(self):
        self.start_dialog('doubleclick')
        btn = self.funq.widget(path='mainWindow::DoubleClickDialog')
        btn.dclick()
        self.assertEquals(self.get_status_text(), 'double clicked !')
