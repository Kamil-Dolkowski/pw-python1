import java.util.ArrayList;
import java.util.List;

public class HotelManagementSystem implements CommandExecutor {
    private static HotelManagementSystem instance;
    private List<Room> rooms = new ArrayList<>();

    private HotelManagementSystem() {}

    public static HotelManagementSystem getInstance() {
        if (instance == null) {
            instance = new HotelManagementSystem();
        }

        return instance;
    }

    public void addRoom(Room newRoom) {
        String newRoomNumber = newRoom.getRoomNumber();

        for (Room room : rooms) {
            if (room.getRoomNumber().equals(newRoomNumber)) {
                System.out.println("# Istnieje już pokój o numerze " + newRoomNumber);
                return;
            }
        }

        rooms.add(newRoom);
        System.out.println("# Dodano pokój nr " + newRoom.getRoomNumber());
    }

    public void removeRoom(String roomNumber) {
        int idx = 0;

        for (Room room : rooms) {
            if (room.getRoomNumber().equals(roomNumber)) {
                break;
            }

            idx++;
        }

        if (idx < rooms.size()) {
            rooms.remove(idx);
            System.out.println("# Usunięto pokój nr " + roomNumber);
            return;
        }

        System.out.println("# Nie można usunąć pokoju (brak takiego pokoju)");
    }

    public void showAllAvailableRooms() {
        System.out.println("\n| ===== DOSTĘPNE POKOJE ===== |");

        int numberOfAvailableRooms = 0;

        for (Room room : rooms) {
            if (room.getIsAvailable() == true) {
                room.info();
                numberOfAvailableRooms++;
            }
        }

        if (numberOfAvailableRooms == 0) {
            System.out.println("Brak dostępnych pokoi");
        } 
    }

    public void reserveRoom(String roomNumber) {
        for (Room room : rooms) {
            if (room.getRoomNumber().equals(roomNumber) && room.getIsAvailable() == true) {
                room.setIsAvailable(false);
                System.out.println("# Zarezerwowano pokój nr " + roomNumber);
                return;
            }
        }

        System.out.println("# Nie można zarezerwować pokoju (brak takiego pokoju)");
    }

    public void cancelReservation(String roomNumber) {
        for (Room room : rooms) {
            if (room.getRoomNumber().equals(roomNumber) && room.getIsAvailable() == false) {
                room.setIsAvailable(true);
                System.out.println("# Cofnięto rezerwację pokoju nr " + roomNumber);
                return;
            }
        }

        System.out.println("# Nie można cofnąć rezerwacji pokoju (brak takiego pokoju)");
    }
}