import java.util.ArrayList;
import java.util.Scanner;

public class AddressBook {
    
    public static void main(String[] args) {
        ArrayList<Contact> contacts = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Select an option:");
            System.out.println("1. Add contact");
            System.out.println("2. View all contacts");
            System.out.println("3. Search contact");
            System.out.println("4. Edit contact");
            System.out.println("5. Delete contact");
            System.out.println("6. Exit");

            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    addContact(contacts, scanner);
                    break;
                case 2:
                    viewAllContacts(contacts);
                    break;
                case 3:
                    searchContact(contacts, scanner);
                    break;
                case 4:
                    editContact(contacts, scanner);
                    break;
                case 5:
                    deleteContact(contacts, scanner);
                    break;
                case 6:
                    System.out.println("Exiting address book...");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please select a valid option.");
            }
        }
    }
    
    public static void addContact(ArrayList<Contact> contacts, Scanner scanner) {
        System.out.println("Enter name:");
        String name = scanner.next();
        
        System.out.println("Enter phone number:");
        String phone = scanner.next();
        
        System.out.println("Enter email address:");
        String email = scanner.next();
        
        if (name.isEmpty() || phone.isEmpty() || email.isEmpty()) {
            System.out.println("Name, phone number, and email address are required fields. Please try again.");
            return;
        }
        
        Contact contact = new Contact(name, phone, email);
        contacts.add(contact);
        System.out.println("Contact added successfully.");
    }
    
    public static void viewAllContacts(ArrayList<Contact> contacts) {
        if (contacts.isEmpty()) {
            System.out.println("No contacts found.");
            return;
        }
        
        System.out.println("All contacts:");
        for (Contact contact : contacts) {
            System.out.println(contact.toString());
        }
    }
    
    public static void searchContact(ArrayList<Contact> contacts, Scanner scanner) {
        System.out.println("Enter name or phone number to search:");
        String search = scanner.next();
        boolean found = false;
        
        for (Contact contact : contacts) {
            if (contact.getName().contains(search) || contact.getPhone().contains(search)) {
                System.out.println(contact.toString());
                found = true;
            }
        }
        
        if (!found) {
            System.out.println("No contacts found.");
        }
    }
    
    public static void editContact(ArrayList<Contact> contacts, Scanner scanner) {
        System.out.println("Enter name or phone number of the contact to edit:");
        String search = scanner.next();
        boolean found = false;
        
        for (Contact contact : contacts) {
            if (contact.getName().contains(search) || contact.getPhone().contains(search)) {
                System.out.println("Enter new name (leave blank to keep current value):");
                String name = scanner.next();
                
                System.out.println("Enter new phone number (leave blank to keep current value):");
                String phone = scanner.next();
                
                System.out.println("Enter new email address (leave blank to keep current value):");
                String email = scanner.next();
            if (!name.isEmpty()) {
                contact.setName(name);
            }
            
            if (!phone.isEmpty()) {
                contact.setPhone(phone);
            }
            
            if (!email.isEmpty()) {
                contact.setEmail(email);
            }
            
            System.out.println("Contact updated successfully.");
            found = true;
            break;
        }
    }
    
    if (!found) {
        System.out.println("No contacts found.");
    }
}

public static void deleteContact(ArrayList<Contact> contacts, Scanner scanner) {
    System.out.println("Enter name or phone number of the contact to delete:");
    String search = scanner.next();
    boolean found = false;

    for (int i = 0; i < contacts.size(); i++) {
        Contact contact = contacts.get(i);
        if (contact.getName().contains(search) || contact.getPhone().contains(search)) {
            contacts.remove(i);
            System.out.println("Contact deleted successfully.");
            found = true;
            break;
        }
    }

    if (!found) {
        System.out.println("No contacts found.");
    }
}}
class Contact {
    private String name;
    private String phone;
    private String email;

    public Contact(String name, String phone, String email) {
        this.name = name;
        this.phone = phone;
        this.email = email;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    @Override
    public String toString() {
        return "Name: " + name + ", Phone: " + phone + ", Email: " + email;
    }
}