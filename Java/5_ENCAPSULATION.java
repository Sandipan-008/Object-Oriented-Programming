
class Account {
    public String name;
    protected String email;
    private String password;

    public String getpassword(){
        return this.password;
    }
    public void setpassword(String Pass){
        this.password = Pass;
    }
 
}
 public class bank{
     public static void main(String args[]){
         Account account1 = new Account();
         account1.name = "apna college";
         account1.email = "apnacollege@gmail.com";
         account1.setpassword("abcd");
         System.out.print(account1.getpassword());
     }
 }
