public interface CommandExecutor {
    public void addRoom(Room newRoom);
    public void removeRoom(String roomNumber);
    public void showAllAvailableRooms();
    public void reserveRoom(String roomNumber);
    public void cancelReservation(String roomNumber);
}