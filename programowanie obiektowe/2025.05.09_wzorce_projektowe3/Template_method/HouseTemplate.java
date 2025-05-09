public abstract class HouseTemplate {
    // Important!!!
    // Preserve creation order
    public final void buildHouse() {
        buildFoundation();
        buildWalls();
        addRoof();
        insertWindowsAndDoors();
        // addRoof(); <-- tutaj bez sensu; najpierw dach, potem okna :)
        System.out.println("House is built");
    }
    
    private void buildFoundation() {
        System.out.println("Build solid foundation for a new house");
    }
    
    private void insertWindowsAndDoors() {
        System.out.println("Insert windows and doors");
    }
    
    public abstract void buildWalls();
    public abstract void addRoof();
}