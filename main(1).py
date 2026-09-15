import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QGraphicsDropShadowEffect


HAPPY_APPLE_STYLE = """
/* Global Window */
QMainWindow {
    background-color: #0c1410;
}

QWidget {
    color: #f1f7f4;
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    font-size: 13px;
}

/* Tab Navigation Bar */
QTabWidget::pane {
    border: 1px solid rgba(118, 255, 3, 0.16);
    background: #111e17;
    border-radius: 14px;
    top: -1px;
}

QTabBar::tab {
    background: transparent;
    color: #8da396;
    padding: 10px 22px;
    font-weight: 700;
    font-size: 13px;
    border-bottom: 3px solid transparent;
    margin-right: 6px;
}

QTabBar::tab:hover {
    color: #76ff03;
    background: rgba(118, 255, 3, 0.08);
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
}

QTabBar::tab:selected {
    color: #76ff03;
    border-bottom: 3px solid #76ff03;
    background: rgba(118, 255, 3, 0.12);
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
}

/* Card Containers */
QFrame#Card {
    background-color: #15251d;
    border: 1px solid rgba(118, 255, 3, 0.22);
    border-radius: 16px;
}

/* Inputs & Selectors */
QLineEdit, QPlainTextEdit, QComboBox {
    background-color: #0a130f;
    border: 1px solid rgba(118, 255, 3, 0.2);
    border-radius: 10px;
    padding: 8px 12px;
    color: #fafffc;
    font-size: 13px;
    selection-background-color: #76ff03;
    selection-color: #0c1410;
}

QLineEdit:focus, QPlainTextEdit:focus, QComboBox:focus {
    border: 1px solid #76ff03;
    background-color: #102117;
}

QComboBox::drop-down {
    border: none;
    padding-right: 10px;
}

QComboBox QAbstractItemView {
    background-color: #15251d;
    border: 1px solid #76ff03;
    selection-background-color: #76ff03;
    selection-color: #0c1410;
    border-radius: 8px;
    outline: none;
}

/* Primary Button: Apple Green to Spring Grass Gradient */
QPushButton#PrimaryBtn {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #76ff03, stop:1 #00e676);
    color: #06180b;
    font-weight: 800;
    font-size: 13px;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
}

QPushButton#PrimaryBtn:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #99ff33, stop:1 #2eff94);
}

QPushButton#PrimaryBtn:pressed {
    background: #00e676;
}

/* Danger / Delete Button */
QPushButton#DangerBtn {
    background-color: rgba(255, 82, 133, 0.12);
    color: #ff5285;
    font-weight: 700;
    border: 1px solid #ff5285;
    border-radius: 8px;
    padding: 8px 16px;
}

QPushButton#DangerBtn:hover {
    background-color: #ff5285;
    color: #ffffff;
}

/* Secondary Button */
QPushButton#SecondaryBtn {
    background-color: rgba(255, 255, 255, 0.05);
    color: #d1fae5;
    border: 1px solid rgba(118, 255, 3, 0.25);
    border-radius: 8px;
    padding: 8px 16px;
    font-weight: 600;
}

QPushButton#SecondaryBtn:hover {
    border-color: #76ff03;
    color: #76ff03;
    background-color: rgba(118, 255, 3, 0.08);
}

/* Data Table */
QTableWidget {
    background-color: #0a130f;
    border: 1px solid rgba(118, 255, 3, 0.14);
    border-radius: 10px;
    gridline-color: rgba(118, 255, 3, 0.08);
    color: #e2fbe8;
}

QHeaderView::section {
    background-color: #15251d;
    color: #a7f3d0;
    padding: 8px;
    font-weight: 700;
    border: none;
    border-bottom: 2px solid #76ff03;
}

/* Status Bar */
QStatusBar {
    background: #0c1410;
    color: #6ee7b7;
    border-top: 1px solid rgba(118, 255, 3, 0.1);
}
"""


def apply_neon_glow(widget, color_hex="#76ff03", blur=22):
    """Soft, lightweight glow effect."""
    shadow = QGraphicsDropShadowEffect(widget)
    shadow.setBlurRadius(blur)
    shadow.setColor(QtGui.QColor(color_hex))
    shadow.setOffset(0, 0)
    widget.setGraphicsEffect(shadow)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 680)
        MainWindow.setStyleSheet(HAPPY_APPLE_STYLE)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.rootLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.rootLayout.setContentsMargins(28, 24, 28, 24)
        self.rootLayout.setSpacing(18)

        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.rootLayout.addWidget(self.tabWidget)

        # ==========================================
        # TAB 1: DASHBOARD
        # ==========================================
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        tab1_layout = QtWidgets.QVBoxLayout(self.tab)
        tab1_layout.setContentsMargins(28, 28, 28, 28)
        tab1_layout.setSpacing(24)

        greeting_layout = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel("Hello,", parent=self.tab)
        self.label.setStyleSheet("font-size: 28px; font-weight: 300; color: #a7f3d0;")
        self.Name = QtWidgets.QLabel("User 🍏", parent=self.tab)
        self.Name.setStyleSheet("font-size: 28px; font-weight: 800; color: #76ff03;")
        greeting_layout.addWidget(self.label)
        greeting_layout.addWidget(self.Name)
        greeting_layout.addStretch()
        tab1_layout.addLayout(greeting_layout)

        hero_card = QtWidgets.QFrame(parent=self.tab)
        hero_card.setObjectName("Card")
        apply_neon_glow(hero_card, "#76ff03", blur=26)
        hero_layout = QtWidgets.QVBoxLayout(hero_card)
        hero_layout.setContentsMargins(26, 26, 26, 26)

        self.label_2 = QtWidgets.QLabel("CURRENT TOTAL BALANCE", parent=hero_card)
        self.label_2.setStyleSheet("font-size: 12px; font-weight: 800; letter-spacing: 1.6px; color: #6ee7b7;")
        hero_layout.addWidget(self.label_2)

        self.Balancel = QtWidgets.QLabel("$0.00", parent=hero_card)
        self.Balancel.setStyleSheet("font-size: 42px; font-weight: 800; color: #ffffff;")
        hero_layout.addWidget(self.Balancel)
        tab1_layout.addWidget(hero_card)

        filter_card = QtWidgets.QFrame(parent=self.tab)
        filter_card.setObjectName("Card")
        filter_layout = QtWidgets.QHBoxLayout(filter_card)
        filter_layout.setContentsMargins(20, 16, 20, 16)

        filter_title = QtWidgets.QLabel("Overview Filter:", parent=filter_card)
        filter_title.setStyleSheet("font-weight: 700; color: #a7f3d0;")
        self.comboBox = QtWidgets.QComboBox(parent=filter_card)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["Income", "Expenses", "Saved"])
        self.comboBox.setFixedWidth(160)

        self.combox = QtWidgets.QLabel("", parent=filter_card)
        self.combox.setStyleSheet("font-size: 18px; font-weight: 700; color: #00e5ff;")

        filter_layout.addWidget(filter_title)
        filter_layout.addWidget(self.comboBox)
        filter_layout.addSpacing(16)
        filter_layout.addWidget(self.combox)
        filter_layout.addStretch()

        tab1_layout.addWidget(filter_card)
        tab1_layout.addStretch()
        self.tabWidget.addTab(self.tab, "Dashboard")

        # ==========================================
        # TAB 2: INCOME
        # ==========================================
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        tab2_layout = QtWidgets.QVBoxLayout(self.tab_2)
        tab2_layout.setContentsMargins(28, 28, 28, 28)

        inc_card = QtWidgets.QFrame(parent=self.tab_2)
        inc_card.setObjectName("Card")
        inc_layout = QtWidgets.QFormLayout(inc_card)
        inc_layout.setContentsMargins(24, 24, 24, 24)
        inc_layout.setVerticalSpacing(16)
        inc_layout.setHorizontalSpacing(20)

        self.label_4 = QtWidgets.QLabel("Amount", parent=inc_card)
        self.amountinc = QtWidgets.QPlainTextEdit(parent=inc_card)
        self.amountinc.setFixedHeight(44)
        self.amountinc.setPlaceholderText("0.00")

        self.label_5 = QtWidgets.QLabel("Source", parent=inc_card)
        self.Source = QtWidgets.QPlainTextEdit(parent=inc_card)
        self.Source.setFixedHeight(44)
        self.Source.setPlaceholderText("e.g., Salary, Dividend, Bonus")

        self.label_6 = QtWidgets.QLabel("Date", parent=inc_card)
        self.Dateinc = QtWidgets.QPlainTextEdit(parent=inc_card)
        self.Dateinc.setFixedHeight(44)
        self.Dateinc.setPlaceholderText("YYYY-MM-DD")

        self.label_7 = QtWidgets.QLabel("Description", parent=inc_card)
        self.Description = QtWidgets.QPlainTextEdit(parent=inc_card)
        self.Description.setFixedHeight(70)
        self.Description.setPlaceholderText("Optional notes...")

        inc_layout.addRow(self.label_4, self.amountinc)
        inc_layout.addRow(self.label_5, self.Source)
        inc_layout.addRow(self.label_6, self.Dateinc)
        inc_layout.addRow(self.label_7, self.Description)

        self.Incsaveb = QtWidgets.QPushButton("Add Income", parent=inc_card)
        self.Incsaveb.setObjectName("PrimaryBtn")
        inc_layout.addRow("", self.Incsaveb)

        tab2_layout.addWidget(inc_card)
        tab2_layout.addStretch()
        self.tabWidget.addTab(self.tab_2, "Income")

        # ==========================================
        # TAB 3: TRANSACTIONS
        # ==========================================
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        tab3_layout = QtWidgets.QVBoxLayout(self.tab_3)
        tab3_layout.setContentsMargins(28, 28, 28, 28)
        tab3_layout.setSpacing(16)

        self.Transactions = QtWidgets.QTableWidget(parent=self.tab_3)
        self.Transactions.setObjectName("Transactions")
        self.Transactions.setColumnCount(4)
        self.Transactions.setHorizontalHeaderLabels(["ID", "Category", "Amount", "Date"])
        self.Transactions.horizontalHeader().setStretchLastSection(True)
        self.Transactions.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        tab3_layout.addWidget(self.Transactions)

        action_card = QtWidgets.QFrame(parent=self.tab_3)
        action_card.setObjectName("Card")
        action_layout = QtWidgets.QHBoxLayout(action_card)
        action_layout.setContentsMargins(18, 14, 18, 14)

        self.label_8 = QtWidgets.QLabel("ID:", parent=action_card)
        self.label_8.setStyleSheet("font-weight: 800; color: #76ff03;")
        self.idtrans = QtWidgets.QLineEdit(parent=action_card)
        self.idtrans.setFixedWidth(110)
        self.idtrans.setPlaceholderText("Target ID")

        self.Edittrans = QtWidgets.QPushButton("Edit", parent=action_card)
        self.Edittrans.setObjectName("SecondaryBtn")
        self.Deltrans = QtWidgets.QPushButton("Delete", parent=action_card)
        self.Deltrans.setObjectName("DangerBtn")

        action_layout.addWidget(self.label_8)
        action_layout.addWidget(self.idtrans)
        action_layout.addSpacing(12)
        action_layout.addWidget(self.Edittrans)
        action_layout.addWidget(self.Deltrans)
        action_layout.addStretch()

        tab3_layout.addWidget(action_card)
        self.tabWidget.addTab(self.tab_3, "Transactions")

        # ==========================================
        # TAB 4: SAVINGS
        # ==========================================
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        tab4_layout = QtWidgets.QHBoxLayout(self.tab_4)
        tab4_layout.setContentsMargins(28, 28, 28, 28)
        tab4_layout.setSpacing(20)

        left_savings = QtWidgets.QFrame(parent=self.tab_4)
        left_savings.setObjectName("Card")
        left_layout = QtWidgets.QVBoxLayout(left_savings)
        left_layout.setContentsMargins(24, 24, 24, 24)

        self.label_9 = QtWidgets.QLabel("SAVINGS GOALS", parent=left_savings)
        self.label_9.setStyleSheet("font-size: 18px; font-weight: 800; color: #ffd600;")
        left_layout.addWidget(self.label_9)

        self.savingcombo = QtWidgets.QComboBox(parent=left_savings)
        self.savingcombo.setObjectName("savingcombo")
        left_layout.addWidget(self.savingcombo)

        left_layout.addSpacing(16)
        stat_grid = QtWidgets.QGridLayout()

        self.Targetl = QtWidgets.QLabel("Target Amount:", parent=left_savings)
        self.Targetl.setStyleSheet("color: #a7f3d0;")
        self.Targetl_2 = QtWidgets.QLabel("$0.00", parent=left_savings)
        self.Targetl_2.setStyleSheet("font-size: 18px; font-weight: 700; color: #ffffff;")

        self.Savedl = QtWidgets.QLabel("Saved So Far:", parent=left_savings)
        self.Savedl.setStyleSheet("color: #a7f3d0;")
        self.Savedl_2 = QtWidgets.QLabel("$0.00", parent=left_savings)
        self.Savedl_2.setStyleSheet("font-size: 18px; font-weight: 800; color: #76ff03;")

        stat_grid.addWidget(self.Targetl, 0, 0)
        stat_grid.addWidget(self.Targetl_2, 0, 1)
        stat_grid.addWidget(self.Savedl, 1, 0)
        stat_grid.addWidget(self.Savedl_2, 1, 1)
        left_layout.addLayout(stat_grid)
        left_layout.addStretch()

        right_savings = QtWidgets.QFrame(parent=self.tab_4)
        right_savings.setObjectName("Card")
        right_layout = QtWidgets.QFormLayout(right_savings)
        right_layout.setContentsMargins(24, 24, 24, 24)
        right_layout.setVerticalSpacing(16)

        form_title = QtWidgets.QLabel("Set New Goal", parent=right_savings)
        form_title.setStyleSheet("font-size: 16px; font-weight: 700; color: #fafffc;")
        right_layout.addRow(form_title)

        self.label_10 = QtWidgets.QLabel("Item Name", parent=right_savings)
        self.itemsave = QtWidgets.QLineEdit(parent=right_savings)
        self.itemsave.setPlaceholderText("e.g. Dream Holiday")

        self.label_11 = QtWidgets.QLabel("Target ($)", parent=right_savings)
        self.targetsave = QtWidgets.QLineEdit(parent=right_savings)
        self.targetsave.setPlaceholderText("e.g. 1000.00")

        self.savinsub = QtWidgets.QPushButton("Submit Goal", parent=right_savings)
        self.savinsub.setObjectName("PrimaryBtn")

        right_layout.addRow(self.label_10, self.itemsave)
        right_layout.addRow(self.label_11, self.targetsave)
        right_layout.addRow("", self.savinsub)

        tab4_layout.addWidget(left_savings, 1)
        tab4_layout.addWidget(right_savings, 1)
        self.tabWidget.addTab(self.tab_4, "Savings")

        # ==========================================
        # TAB 5: EXPENSES (with Live Balance Preview)
        # ==========================================
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        tab5_layout = QtWidgets.QVBoxLayout(self.tab_5)
        tab5_layout.setContentsMargins(28, 28, 28, 28)
        tab5_layout.setSpacing(20)

        # Cheerful Balance Comparison Card
        exp_balance_card = QtWidgets.QFrame(parent=self.tab_5)
        exp_balance_card.setObjectName("Card")
        apply_neon_glow(exp_balance_card, "#76ff03", blur=20)
        exp_card_layout = QtWidgets.QHBoxLayout(exp_balance_card)
        exp_card_layout.setContentsMargins(24, 20, 24, 20)

        # Current Balance (Fresh Apple Green)
        curr_box = QtWidgets.QVBoxLayout()
        self.exp_current_balance_lbl = QtWidgets.QLabel("CURRENT BALANCE", parent=exp_balance_card)
        self.exp_current_balance_lbl.setStyleSheet("font-size: 11px; font-weight: 800; letter-spacing: 1.2px; color: #6ee7b7;")
        self.exp_current_balance_val = QtWidgets.QLabel("$0.00", parent=exp_balance_card)
        self.exp_current_balance_val.setStyleSheet("font-size: 28px; font-weight: 800; color: #76ff03;")
        curr_box.addWidget(self.exp_current_balance_lbl)
        curr_box.addWidget(self.exp_current_balance_val)
        exp_card_layout.addLayout(curr_box)

        # Subtle Vertical Divider
        v_sep = QtWidgets.QFrame(parent=exp_balance_card)
        v_sep.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        v_sep.setStyleSheet("background-color: rgba(118, 255, 3, 0.2);")
        exp_card_layout.addWidget(v_sep)

        # Balance After Expense (Electric Sky Blue / Cheerful Coral)
        rem_box = QtWidgets.QVBoxLayout()
        self.exp_remaining_balance_lbl = QtWidgets.QLabel("BALANCE AFTER EXPENSE", parent=exp_balance_card)
        self.exp_remaining_balance_lbl.setStyleSheet("font-size: 11px; font-weight: 800; letter-spacing: 1.2px; color: #6ee7b7;")
        self.exp_remaining_balance_val = QtWidgets.QLabel("$0.00", parent=exp_balance_card)
        self.exp_remaining_balance_val.setStyleSheet("font-size: 28px; font-weight: 800; color: #00e5ff;")
        rem_box.addWidget(self.exp_remaining_balance_lbl)
        rem_box.addWidget(self.exp_remaining_balance_val)
        exp_card_layout.addLayout(rem_box)

        tab5_layout.addWidget(exp_balance_card)

        # Expense Form Card
        exp_card = QtWidgets.QFrame(parent=self.tab_5)
        exp_card.setObjectName("Card")
        exp_layout = QtWidgets.QFormLayout(exp_card)
        exp_layout.setContentsMargins(24, 24, 24, 24)
        exp_layout.setVerticalSpacing(16)

        header_exp = QtWidgets.QHBoxLayout()
        exp_title = QtWidgets.QLabel("Log Expense", parent=exp_card)
        exp_title.setStyleSheet("font-size: 16px; font-weight: 700; color: #fafffc;")
        self.xpenses = QtWidgets.QLabel("", parent=exp_card)
        self.xpenses.setStyleSheet("font-size: 16px; font-weight: 700; color: #ff5252;")
        header_exp.addWidget(exp_title)
        header_exp.addStretch()
        header_exp.addWidget(self.xpenses)
        exp_layout.addRow(header_exp)

        self.label_3 = QtWidgets.QLabel("Amount", parent=exp_card)
        self.amxpense = QtWidgets.QLineEdit(parent=exp_card)
        self.amxpense.setPlaceholderText("0.00")

        self.label_12 = QtWidgets.QLabel("Date", parent=exp_card)
        self.date = QtWidgets.QLineEdit(parent=exp_card)
        self.date.setPlaceholderText("YYYY-MM-DD")

        # Cheerful Sunburst gradient for expense submit button
        self.xpenseb = QtWidgets.QPushButton("Add Expense", parent=exp_card)
        self.xpenseb.setObjectName("PrimaryBtn")
        self.xpenseb.setStyleSheet(
            "background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #ff9100, stop:1 #ff5252);"
            "color: #ffffff; font-weight: 800; font-size: 13px; border-radius: 10px; padding: 10px 20px;"
        )

        exp_layout.addRow(self.label_3, self.amxpense)
        exp_layout.addRow(self.label_12, self.date)
        exp_layout.addRow("", self.xpenseb)

        tab5_layout.addWidget(exp_card)
        tab5_layout.addStretch()
        self.tabWidget.addTab(self.tab_5, "Expenses")

        # Interactive Balance Calculator Connection
        self.amxpense.textChanged.connect(self._update_expense_preview)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.tabWidget.setCurrentIndex(4)  # Shows Expenses view first
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setWindowTitle("FinTrack // Fresh Apple")

    def _update_expense_preview(self):
        """Dynamically computes Balance - Expense with responsive happy/warning colors."""
        try:
            bal_text = self.Balancel.text().replace("$", "").replace(",", "").strip()
            current_bal = float(bal_text) if bal_text else 0.00
        except ValueError:
            current_bal = 0.00

        try:
            exp_text = self.amxpense.text().replace("$", "").replace(",", "").strip()
            expense_amt = float(exp_text) if exp_text else 0.00
        except ValueError:
            expense_amt = 0.00

        rem_bal = current_bal - expense_amt

        self.exp_current_balance_val.setText(f"${current_bal:,.2f}")
        self.exp_remaining_balance_val.setText(f"${rem_bal:,.2f}")

        # If negative, shifts to coral pink; otherwise shines in bright happy cyan
        if rem_bal < 0:
            self.exp_remaining_balance_val.setStyleSheet("font-size: 28px; font-weight: 800; color: #ff5252;")
        else:
            self.exp_remaining_balance_val.setStyleSheet("font-size: 28px; font-weight: 800; color: #00e5ff;")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())