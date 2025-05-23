public class CommandProxy implements CommandExecutor {
    private CommandExecutor executor;
    private boolean isPrivileged;
    
    public CommandProxy(String login, String password) {
        if (login.equals("employee") && password.equals("hotel123")) {
            isPrivileged = true;
        } else {
            isPrivileged = false;
        }
        
        executor = HotelManagementSystem.getInstance();
    }

    public void addRoom(Room newRoom) {
        if (isPrivileged == true) {
            executor.addRoom(newRoom);
        } else {
            System.out.println("(!) Nie masz uprawnień do użycia tego polecenia");
        }
    }

    public void removeRoom(String roomNumber) {
        if (isPrivileged == true) {
            executor.removeRoom(roomNumber);
        } else {
            System.out.println("(!) Nie masz uprawnień do użycia tego polecenia");
        }
    }

    public void showAllAvailableRooms() {
        executor.showAllAvailableRooms();
    }

    public void reserveRoom(String roomNumber) {
        if (isPrivileged == true) {
            executor.reserveRoom(roomNumber);
        } else {
            System.out.println("(!) Nie masz uprawnień do użycia tego polecenia");
        }
    }

    public void cancelReservation(String roomNumber) {
        if (isPrivileged == true) {
            executor.cancelReservation(roomNumber);
        } else {
            System.out.println("(!) Nie masz uprawnień do użycia tego polecenia");
        }
    }
}