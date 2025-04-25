public class MySQLHelper {
    public static Connection getMySQLDBConnection() {
        return new Connection("MySQL");
    }
    
    public void generateMySQLPDFReport(Connection con, String table, String outFileName) {
        System.out.println("Get data from MySQL table '" + table + "', generate report in PDF format and save as '" + outFileName + "'");
    }
    
    public void generateMySQLRawDataCSV(Connection con, String table, String outFileName) {
        System.out.println("Get raw data from MySQL table '" + table + "' in CSV format and save as '" + outFileName + "'");
    }
}