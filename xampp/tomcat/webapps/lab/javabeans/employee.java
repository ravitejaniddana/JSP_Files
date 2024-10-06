package college;

public class employee {
    private String name = "ravi";
    private String department = "cse";

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) { // Change here: 'SetDepartment' to 'setDepartment'
        this.department = department; // Also corrected to assign 'dept' to 'department'
    }
}
