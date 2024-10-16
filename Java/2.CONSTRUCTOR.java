 // constructor 1 [normal]
class student{
    String name;
    int age;
    public void info(){
            System.out.println(this.name);
            System.out.println(this.age);
    }
    student(){
     System.out.println("constructor called");
    }
    
}
      
public class std{
    public static void main(String[]args){
        student s1 = new student();
        s1.name = "sandipan";
        s1.age = 22;
        s1.info();
    }
} 

//>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>...
// constructor 2 [parametirized]
class student{
    String name;
    int age;                    //declaring variable
     public void info(){
            System.out.println(this.name);
            System.out.println(this.age);
    }
    student(String name, int age){
     this.name=name;
     this.age=age;
    }
    
}
    
public class std{
    public static void main(String[]args){
        student s1 = new student("sandipan",22);
        s1.info();
    }
}  

//>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>...
// constructor 3 [copy constructor]
class student{
    String name;
    int age;
     public void info(){
            System.out.println("his name: "+this.name);
            System.out.println("his age: "+this.age);
    }
    student(student s2){
     this.name=s2.name;
     this.age=s2.age;
    }
    student(){
     }
    
}
public class std{
    public static void main(String[]args){
        student s1 = new student();
        s1.name = "sandipan";
        s1.age = 22;
        student s2 = new student(s1);
        s2.info();
        
    }
}
    
