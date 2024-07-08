class pen{
   //constructor
  String color;
   String type;
   public void write(){ //class method_1
          System.out.println("writing something");
}
   public void colorprint(){ //class method_2
          System.out.println(this.color);
}
}

public class oop{
    public static void main(String args[]){
       pen pen1 = new pen();//assigning class to object1 of same class
       pen1.color = "blue";
       pen1.type = "gel";
       pen1.colorprint();
       pen1.write();
       
       pen pen2 = new pen(); //assigning class to object2 of same class
       pen2.color = "black";
       pen2.type = "dot";
       pen2.colorprint();
      
    }
    
}
//>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..
class student{
    String name;
    String roll_no;
    public void study(){
        System.out.println(this.name+" is studying math");
    }
     public void grade(){
        System.out.println(this.name+" got grade A");
    }
     public void promote(){
        System.out.println("roll no-"+this.roll_no+" is promoted to class 10");
    }
}
    
public class std{
    public static void main(String[]args){
        student s1 = new student();
        s1.name = "ram";
        s1.roll_no = "101";
        s1.study();
        student s2 = new student();
        s2.name = "suman";
        s2.roll_no = "111";
        s2.grade();
        student s3 = new student();
        s3.name = "kiran";
        s3.roll_no = "112";
        s3.promote();

    }
}  
//>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..
    
class calculator{
    int i1 ;
    int i2 ;
    public void addition(){
        System.out.println("addition is: "+(this.i1+this.i2));
    }
}    
    
public class number{
    public static void main (String[]args){
        calculator exp = new calculator();
        exp.i1 = 5;
        exp.i2 = 9;
        exp.addition();
    
    }
}
//>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..
