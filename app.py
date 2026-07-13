"""
Main application entry point
Orchestrates the application flow
"""

from services import InventoryService
from ui import InventoryUI


class InventoryApplication:
    """Main application controller"""
    
    def __init__(self):
        """Initialize application"""
        self.service = InventoryService()
        self.ui = InventoryUI(self.service)
        self.running = False
    
    def run(self) -> None:
        """Run the application"""
        self.running = True
        self.ui.show_welcome()
        
        while self.running:
            try:
                self.ui.show_menu()
                choice = self.ui.formatter.get_menu_choice()
                self.handle_menu_choice(choice)
            except KeyboardInterrupt:
                print("\n\n✓ Application interrupted by user. Goodbye!\n")
                self.running = False
            except Exception as e:
                print(f"\n✗ An error occurred: {e}")
                print("Please try again.\n")
    
    def handle_menu_choice(self, choice: str) -> None:
        """
        Handle menu choice
        
        Args:
            choice: User's menu choice
        """
        if choice == '1':
            self.ui.show_add_product_screen()
        elif choice == '2':
            self.ui.show_products_screen()
        elif choice == '3':
            self.ui.show_search_screen()
        elif choice == '4':
            self.ui.show_update_stock_screen()
        elif choice == '5':
            self.ui.show_delete_screen()
        elif choice == '6':
            self.ui.show_report_screen()
        elif choice == '7':
            self.ui.show_backup_screen()
        elif choice == '8':
            print("\n✓ Thank you for using Shwapno Inventory Management System!")
            print("Goodbye!\n")
            self.running = False
        else:
            print("✗ Invalid choice! Please select 1-8.")


def main():
    """Application entry point"""
    app = InventoryApplication()
    app.run()


if __name__ == "__main__":
    main()