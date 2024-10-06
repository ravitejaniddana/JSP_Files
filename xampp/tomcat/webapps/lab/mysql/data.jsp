<%@ page import="java.sql.*" %>
<!DOCTYPE html>
<html>
<body>
    <%
        String url = "jdbc:mysql://localhost:3306/demoDB"; // Ensure this is your database name
        Connection conn = null;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver"); // Updated driver class name
            conn = DriverManager.getConnection(url, "root", ""); // Update your username and password
            Statement st = conn.createStatement();
            String query = "SELECT * FROM employee";
            ResultSet rs = st.executeQuery(query);
            while (rs.next()) {
                out.println("Empy_Id : " + rs.getInt("Empy_Id"));
                out.println("<br> FirstName: " + rs.getString("first_name"));
                out.println("<br> LastName: " + rs.getString("last_name"));
            }
        } catch (Exception e) {
            out.println("Error: " + e.getMessage());
        } finally {
            if (conn != null) {
                conn.close();
            }
        }
    %>
</body>
</html>

INSERT INTO employee (emp_id, first_name, last_name)
VALUES (1, 'John', 'Doe'),
       (2, 'Jane', 'Smith'),
       (3, 'Robert', 'Brown'),
       (4, 'Emily', 'Johnson'),
       (5, 'Michael', 'Davis'),
       (6, 'Linda', 'Williams');
