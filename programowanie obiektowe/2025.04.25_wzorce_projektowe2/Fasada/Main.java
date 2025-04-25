public class Main
{
	public static void main(String[] args) {
		Connection con1 = MySQLHelper.getMySQLDBConnection();
		MySQLHelper storage1 = new MySQLHelper();
		storage1.generateMySQLPDFReport(con1, "TBL_PERSON", "person.pdf");
		
		Connection con2 = JSONHelper.getJSONConnection();
		JSONHelper storage2 = new JSONHelper();
		storage2.generateJSONPDFReport(con2, "person.json", "person.pdf");
		
		System.out.println("-----------------------------------------");
		
		Facade.generateOutput(Facade.StorageType.MYSQL, Facade.OutputType.REPORT_PDF, "person", "person.pdf");
		Facade.generateOutput(Facade.StorageType.JSON, Facade.OutputType.REPORT_PDF, "person", "person.pdf");
	}
}