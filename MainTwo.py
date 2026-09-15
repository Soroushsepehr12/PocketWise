import sys
import datetime
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from main import Ui_MainWindow
conn = sqlite3.connect('PW.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    created_at TEXT NOT NULL

)''')
conn.commit()
cursor.execute('''CREATE TABLE IF NOT EXISTS balance(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    balance INT NOT NULL

)''')
conn.commit()
cursor.execute('''CREATE TABLE IF NOT EXISTS income(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount INT NOT NULL,
    source TEXT NOT NULL,
    date TEXT NOT NULL,
    des TEXT

)''')
conn.commit()
cursor.execute('''CREATE TABLE IF NOT EXISTS saving(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    target TEXT NOT NULL,
    amount INT NOT NULL,
    date TEXT NOT NULL

)''')
conn.commit()
cursor.execute('''CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount INT NOT NULL,
    date TEXT NOT NULL

)''')
conn.commit()
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setname()
        self.ui.Incsaveb.clicked.connect(lambda: self.addinc(
            self.ui.amountinc.toPlainText(),
            self.ui.Source.toPlainText(),
            self.ui.Dateinc.toPlainText(),
            self.ui.Description.toPlainText()
        ))
        self.setbalance()
        self.transc()
        self.ui.comboBox.currentIndexChanged.connect(lambda: self.setcombobox())
        self.x()
        self.ui.xpenseb.clicked.connect(self.addx)
        self.savings()
        self.ui.savinsub.clicked.connect(self.addsaving)
    def setname(self):
        cursor.execute('SELECT name FROM users')
        row = cursor.fetchone()
        self.ui.Name.setText(row[0] if row else "Guest")
    def get_total(self, table, column='amount'):
        cursor.execute(f'SELECT {column} FROM {table}')
        rows = cursor.fetchall()
        total = 0
        for row in rows:
            try:
                total += int(row[0])
            except(TypeError, ValueError):
                continue
        return total
    def warn(self, message):
        QMessageBox.warning(self, "INvalid Input", message)
    def setbalance(self):
        incometotal = self.get_total('income')
        expensetotal = self.get_total('expenses')
        balance = incometotal - expensetotal
        self.ui.Balancel.setText(str(balance))
    def addinc(self, amount, source, date, des):
        amount = amount.strip()
        source = source.strip()
        date = str(date).strip()
        des = des.strip()
        if not amount.lstrip('-').isdigit():
            self.warn("AMOUNT MUST BE A WHOLE NUMBER")
            return
        if not source:
            self.warn("Please enter a source for this income.")
            return
        if not date:
            self.warn("Please enter a date.")
            return
        cursor.execute(
            '''
            INSERT INTO income(amount, source, date, des)
            VALUES (?, ?, ?, ?)
            ''',
            (int(amount), source, date, des)
        )
        conn.commit()
        self.ui.amountinc.clear()
        self.ui.Source.clear()
        self.ui.Description.clear()
        self.setbalance()
        self.transc()
        self.x()
        self.savings()
    def transc(self):
        table = self.ui.Transactions
        cursor.execute('SELECT id, amount, source, date, des FROM income')
        rec = cursor.fetchall()
        table.setRowCount(0)
        for row_idx, rowdata in enumerate(rec):
            table.insertRow(row_idx)
            for col_idx, value in enumerate(rowdata):
                item = QTableWidgetItem(str(value))
                table.setItem(row_idx, col_idx, item)
    def setcombobox(self):
        income_total = self.get_total('income')
        if self.ui.comboBox.currentIndex() == 0:
            self.ui.combox.setText(str(income_total))
    def x(self):
        income_total = self.get_total('income')
        expense_total = self.get_total('expenses')
        self.ui.exp_current_balance_val.setText(str(income_total))
        self.ui.exp_remaining_balance_val.setText(str(income_total - expense_total))
    def addx(self):
        amount = self.ui.amxpense.text().strip()
        date = self.ui.date.text().strip()
        if not amount.lstrip('-').isdigit():
            self.warn("Expense amount must be a whole number.")
            return
        cursor.execute('INSERT INTO expenses(amount, date) VALUES(?,?)', (int(amount), date))
        conn.commit()
        self.x()
        self.setbalance()
        self.savings()
    def savings(self):
        target_total = self.get_total('saving')
        income_total = self.get_total('income')
        expense_total = self.get_total('expenses')
        saved = income_total - expense_total - target_total
        self.ui.Targetl_2.setText(str(target_total))
        self.ui.Savedl_2.setText(str(saved))
    def addsaving(self):
        name = self.ui.itemsave.text().strip()
        target = self.ui.targetsave.text().strip()
        if not name:
            self.warn("Please input the name: ")
            return
        if not target.lstrip('-').isdigit():
            self.warn("It must be a number")
            return
        today = str(datetime.date.today())
        cursor.execute("INSERT INTO saving(target, amount, date) VALUES(?, ?, ?)", (name, int(target), today))
        conn.commit()
    
app = QApplication(sys.argv)
window  = Mainwindow()
window.show()
sys.exit(app.exec())