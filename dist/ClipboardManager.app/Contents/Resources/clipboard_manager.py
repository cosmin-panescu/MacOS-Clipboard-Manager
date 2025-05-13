import rumps
import pyperclip
import threading
import time
from Foundation import NSPasteboard

class ClipboardManagerApp(rumps.App):
    def __init__(self):
        super(ClipboardManagerApp, self).__init__("📋")
        
        self.clipboard_history = []
        self.last_clipboard_content = pyperclip.paste()
        self.last_check_time = time.time()
        self._menu_update_needed = False
        
        self.pasteboard = NSPasteboard.generalPasteboard()
        self.last_change_count = self.pasteboard.changeCount()
        
        self.clipboard_thread = threading.Thread(target=self.monitor_clipboard)
        self.clipboard_thread.daemon = True
        self.clipboard_thread.start()
        
        self.timer = rumps.Timer(self.check_menu_update, 0.5)
        self.timer.start()
    
    def monitor_clipboard(self):
        min_sleep_time = 0.5 
        max_sleep_time = 2.0  
        current_sleep_time = min_sleep_time
        
        while True:
            try:
                # Verify if there are changes in the clipboard
                current_change_count = self.pasteboard.changeCount()
                
                if current_change_count != self.last_change_count:
                    self.last_change_count = current_change_count
                    
                    current_content = pyperclip.paste()
                    if current_content != self.last_clipboard_content and current_content.strip():
                        self.process_new_content(current_content)
                        self.last_clipboard_content = current_content
                    
                    # Reset sleep time to minimum when there is a change
                    current_sleep_time = min_sleep_time
                    self.last_check_time = time.time()
                else:
                    # Increase the sleep time if no changes are detected
                    elapsed = time.time() - self.last_check_time
                    if elapsed > 10:  
                        current_sleep_time = min(current_sleep_time * 1.1, max_sleep_time)
                
                time.sleep(current_sleep_time)
            except Exception as e:
                print(f"Eroare in monitor_clipboard: {e}")
                time.sleep(1) 
    
    def process_new_content(self, content):
        try:
            # Limit text length
            if len(content) > 10000: 
                content = content[:10000]
                
            # Delete duplicates 
            if content in self.clipboard_history:
                self.clipboard_history.remove(content)
            
            # Add the new content to the beginning of the history
            self.clipboard_history.insert(0, content)
            
            # Only 10 copied items
            while len(self.clipboard_history) > 10:
                self.clipboard_history.pop()
            
            self._menu_update_needed = True
            print(f"Adaugat in istoric: {content[:50]}")  # Debug
        except Exception as e:
            print(f"Eroare in process_new_content: {e}")
    
    def check_menu_update(self, _):
        if self._menu_update_needed:
            self.update_menu()
            self._menu_update_needed = False
    
    def update_menu(self):
        try:
            quit_button = None
            for item in self.menu:
                if item.title == 'Quit':
                    quit_button = item
                    break
            
            # Clear menu completely
            self.menu.clear()
            
            # Add elements from history
            for content in self.clipboard_history:
                # Limit text length for display
                display_text = content if len(content) < 50 else content[:47] + "..."
                self.menu.add(rumps.MenuItem(display_text, callback=self.copy_from_history))
            
            # Add Clear History and Quit buttons
            if self.clipboard_history:
                self.menu.add(rumps.separator)
                self.menu.add(rumps.MenuItem("Clear History", callback=self.clear_history))
            
            # Add separator and Quit button
            self.menu.add(rumps.separator)
            if quit_button:
                self.menu.add(quit_button)
            else:
                self.menu.add(rumps.MenuItem("Quit", callback=self.quit_app))
            
            print(f"Meniu actualizat, {len(self.clipboard_history)} elemente")  # Debug
        except Exception as e:
            print(f"Eroare in update_menu: {e}")
    
    def copy_from_history(self, sender):
        try:
            # Find the content in the history and copy it to the clipboard
            for content in self.clipboard_history:
                if sender.title == content or sender.title == content[:47] + "...":
                    pyperclip.copy(content)
                    self.last_clipboard_content = content
                    self.last_change_count = self.pasteboard.changeCount()  
                    break
        except Exception as e:
            print(f"Error in copy_from_history: {e}")
    
    def clear_history(self, _):
        # Clear the clipboard history
        self.clipboard_history = []
        self.update_menu()
    
    def quit_app(self, _):
        """Quit the application."""
        rumps.quit_application()

if __name__ == "__main__":
    app = ClipboardManagerApp()
    app.run(debug=False)
