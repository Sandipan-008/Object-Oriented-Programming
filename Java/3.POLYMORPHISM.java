class student{
    String name;
    int age;                //declaring variables
    
     public void info(String name){
         System.out.println(name);
     }
       public void info(int age){
         System.out.println(age);
     }
       public void info(String name,int age){
         System.out.println(name+" "+age);
     }
     
}
    
public class std{
    public static void main(String[]args){
        student s1 = new student();
        s1.name="sandipan";
        s1.age=22;
        s1.info(s1.name,s1.age);
    }
} 
