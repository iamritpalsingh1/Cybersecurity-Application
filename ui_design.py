from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget
from PyQt5 import QtCore
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralWidget = QWidget(MainWindow)
        self.layout = QVBoxLayout(self.centralWidget)

        self.nameLabel = QLabel("Name:", self.centralWidget)
        self.layout.addWidget(self.nameLabel)
        self.nameInput = QLineEdit(self.centralWidget)
        self.layout.addWidget(self.nameInput)

        self.emailLabel = QLabel("Email:", self.centralWidget)
        self.layout.addWidget(self.emailLabel)
        self.emailInput = QLineEdit(self.centralWidget)
        self.layout.addWidget(self.emailInput)

        self.issueLabel = QLabel("Describe the Issue:", self.centralWidget)
        self.layout.addWidget(self.issueLabel)
        self.issueInput = QTextEdit(self.centralWidget)
        self.layout.addWidget(self.issueInput)

        self.submitButton = QPushButton("Submit Ticket", self.centralWidget)
        self.layout.addWidget(self.submitButton)
        
        
        # ... existing UI code ...

        self.trackIssueLabel = QLabel("Enter Issue Key:", self.centralWidget)
        self.layout.addWidget(self.trackIssueLabel)

        self.trackIssueInput = QLineEdit(self.centralWidget)
        self.layout.addWidget(self.trackIssueInput)

        self.trackIssueButton = QPushButton("Track Issue", self.centralWidget)
        self.layout.addWidget(self.trackIssueButton)
        self.trackIssueButton.clicked.connect(self.onTrackIssue)

        self.issueDetailsOutput = QTextEdit(self.centralWidget)
        self.issueDetailsOutput.setReadOnly(True)  # Make it read-only
        self.layout.addWidget(self.issueDetailsOutput)

# ... rest of UI setup code ...

        

        MainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ITSM Service Ticket Tracker"))