import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_design import Ui_MainWindow
from api.itsm_api import ITSM_API

class ServiceTicketApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ServiceTicketApp, self).__init__()
        self.setupUi(self)
        
        # Initialize the API with your JIRA details
        self.itsm_api = ITSM_API(
            email='jblxboat2@gmail.com',
            api_token='ATATT3xFfGF0kOhaSMLEpcsR4Gjta3GfTlBF5f0WAL6PO8Y9xgVq46eQ25HjDijV0IW_6MPUTEWGs49Eg1u9o9_7yfgJG7CyxQ2M3N3bgdvI3cbu_CHj6eVoeIompuvgAeUrXY1sgZwPfcXV36MFgfCTNTZKfY9VH36coFrjTGXfCUczBIuFjmA=15EB0B72',
            base_url='https://jblxboat2.atlassian.net/rest/api/3'
        )
        
        self.submitButton.clicked.connect(self.onSubmit)

    def onSubmit(self):
        description = self.issueInput.toPlainText() if self.issueInput else "No description provided."
        summary =description[:50] if len(description) > 50 else "New Issue - details in description"
        project_key = "SCRUM"  # Replace with your actual JIRA project key
        issue_type = "Bug" # Replace with your actual issue type

        # Call the API to create a ticket
        response = self.itsm_api.create_issue(summary, project_key, issue_type, description)
        if response and 'key' in response:
            QMessageBox.information(self, 'Success', f'Ticket created successfully! Ticket ID: {response["key"]}')
            # Clear the input fields or take additional actions
        else:
            QMessageBox.warning(self, 'Error', f'Failed to create ticket. Response: {response}')
    def onTrackIssue(self):
        issue_key = self.trackIssueInput.text()
        if issue_key:
            issue_details = self.itsm_api.get_issue_details(issue_key)
            if issue_details:
                # Format and display the issue details in the UI
                formatted_details = self.format_issue_details(issue_details)
                self.issueDetailsOutput.setPlainText(formatted_details)
            else:
                QMessageBox.warning(self, 'Error', 'Failed to retrieve issue details.')
        else:
            QMessageBox.warning(self, 'Error', 'Please enter an issue key.')

    def format_issue_details(self, details):
        # Format the details dictionary into a human-readable string
        # This is just a placeholder, you'll need to adjust based on the actual response structure
        formatted = f"Issue Key: {details['key']}\nSummary: {details['fields']['summary']}\nStatus: {details['fields']['status']['name']}"
        return formatted
    
    
    
def main():
    app = QApplication(sys.argv)
    ex = ServiceTicketApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
