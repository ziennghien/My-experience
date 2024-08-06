import java.util.*;
import java.io.*;

public class TransactionProcessing {
    private ArrayList<Payment> paymentObjects;
    private IDCardManagement idcm;
    
    public TransactionProcessing(String idCardPath, String paymentPath) {
        idcm = new IDCardManagement(idCardPath);
        readPaymentObject(paymentPath);
    
    }

    public ArrayList<Payment> getPaymentObject() {
        return this.paymentObjects;
    }

    // Requirement 3
    public boolean readPaymentObject(String path) {
        try {
            paymentObjects=new ArrayList<Payment>();
            File f = new File(path);
            Scanner sc = new Scanner(f);
            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                if(line.contains(",")){
                    String[] components = line.split(",");
                    paymentObjects.add(new BankAccount(Integer.parseInt(components[0]),Double.parseDouble(components[1])));
                }
                else{
                    if(line.length()==6){
                        for(IDCard idc: idcm.getIDCards()){
                            try{
                                if(idc.getSoDinhDanh()==Integer.valueOf(line)){
                                    paymentObjects.add(new ConvenientCard(idc));
                                }
                            }catch(CannotCreateCard e) {
                                System.out.println(e);
                                continue;
                            }
                        }
                    }
                    else{
                        paymentObjects.add(new EWallet(Integer.valueOf(line)));
                    }
                }
            }
            sc.close();
            return true;
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
        
    }

    // Requirement 4
    public ArrayList<ConvenientCard> getAdultConvenientCards() {
        ArrayList<ConvenientCard> rs=new ArrayList<ConvenientCard>();
        for(Payment tem: getPaymentObject()){
            if(tem instanceof ConvenientCard){
                try{
                    String type=((ConvenientCard)tem).getType();
                    if(type.equals("Adult"))
                        rs.add((ConvenientCard)tem);
                }catch (CannotCreateCard e) {
                    System.out.println(e);
                    continue;
                }
            }
        }
        return rs;
    }

    // Requirement 5
    public ArrayList<IDCard> getCustomersHaveBoth() {
        ArrayList<IDCard> rs= new ArrayList<IDCard>();
        for(IDCard idc: idcm.getIDCards()){
            int ss=0;
            for(Payment tem: getPaymentObject()){
                if(tem instanceof BankAccount){
                    if(idc.getSoDinhDanh()==((BankAccount)tem).getSTK()){
                        ss++;
                    } 
                }
                if(tem instanceof ConvenientCard){
                    if(idc.getSoDinhDanh()==((ConvenientCard)tem).getDinhDanh()){
                        ss++;
                    }
                }
                if(tem instanceof EWallet){
                    if(idc.getSDT()==((EWallet)tem).getDT()){
                        ss++;
                    }
                }
            }
            if(ss==3){
                rs.add(idc);
            }
        }
        return rs;
    }

    // Requirement 6
    public void processTopUp(String path) {
        try {
            File f = new File(path);
            Scanner sc = new Scanner(f);
            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                String[] components = line.split(",");
                for(Payment tem: getPaymentObject()){
                    if(components[0].equals("BA")){
                        if(tem instanceof BankAccount){
                            if(((BankAccount)tem).getSTK()==Integer.valueOf(components[1])){
                                ((BankAccount)tem).topUp(Integer.valueOf(components[2]));
                                break;
                            }
                        }
                    }
                    if(components[0].equals("CC")){
                        if(tem instanceof ConvenientCard){
                            if(((ConvenientCard)tem).getDinhDanh()==Integer.valueOf(components[1])){
                                ((ConvenientCard)tem).topUp(Integer.valueOf(components[2]));
                                break;
                            }
                        }
                    }
                    if(components[0].equals("EW")){
                        if(tem instanceof EWallet){
                            if(((EWallet)tem).getDT()==Integer.valueOf(components[1])){
                                ((EWallet)tem).topUp(Integer.valueOf(components[2]));
                                break;
                            }
                        }
                    }
                }
            }
            sc.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Requirement 7
    public ArrayList<Bill> getUnsuccessfulTransactions(String path) {
        ArrayList<Bill> rs=new ArrayList<Bill>();
        try {
            File f = new File(path);
            Scanner sc = new Scanner(f);
            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                String[] components = line.split(",");
                
                if(components[3].equals("BA")){
                    for(Payment tem: getPaymentObject()){
                        if(tem instanceof BankAccount){
                            if(Integer.valueOf(components[4])==((BankAccount)tem).getSTK()){
                                if(((BankAccount)tem).pay(Double.valueOf(components[1]))==false){
                                    Bill loi=new Bill(Integer.valueOf(components[0]),Double.valueOf(components[1]),components[2]);
                                    rs.add(loi);
                                    break;
                                }
                            }
                        }
                    }
                }
                if(components[3].equals("CC")){
                    for(Payment tem: getPaymentObject()){
                        if(tem instanceof ConvenientCard){
                            if(Integer.valueOf(components[4])==((ConvenientCard)tem).getDinhDanh()){
                                if(((ConvenientCard)tem).pay(Double.valueOf(components[1]))==false){
                                    Bill loi=new Bill(Integer.valueOf(components[0]),Double.valueOf(components[1]),components[2]);
                                    rs.add(loi);
                                    break;
                                }
                            }
                        }
                    }
                }
                if(components[3].equals("EW")){
                    for(Payment tem: getPaymentObject()){
                        if(tem instanceof EWallet){
                            if(Integer.valueOf(components[4])==((EWallet)tem).getDT()){
                                if(((EWallet)tem).pay(Double.valueOf(components[1]))==false){
                                    Bill loi=new Bill(Integer.valueOf(components[0]),Double.valueOf(components[1]),components[2]);
                                    rs.add(loi);
                                    break;
                                }
                            }
                        }
                    }
                }
                
            }
            sc.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return rs;
    }

    // Requirement 8
    public ArrayList<BankAccount> getLargestPaymentByBA(String path) {
        ArrayList<BankAccount> rs=new ArrayList<BankAccount>();
        double max=0,tien;
        try {
            File f = new File(path);
            Scanner sc = new Scanner(f);
            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                String[] components = line.split(",");
                
                
                if(components[3].equals("BA")){
                    for(Payment tem: getPaymentObject()){
                        if(tem instanceof BankAccount){
                            if(Integer.valueOf(components[4])==((BankAccount)tem).getSTK()){
                                if(((BankAccount)tem).pay(Double.valueOf(components[1]))){
                                    tien=Double.valueOf(components[1]);
                                    if(tien>max){
                                        max=tien;
                                        rs.clear();
                                        rs.add((BankAccount)tem);
                                    }
                                    if(tien==max){
                                        if(rs.contains(tem)==false)
                                            rs.add((BankAccount)tem);
                                    }
                                }
                            }
                        }
                    }
                }
                
            }
            sc.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return rs;
    }

    //Requirement 9
    public void processTransactionWithDiscount(String path) {
        try {
            File f = new File(path);
            Scanner sc = new Scanner(f);
            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                String[] components = line.split(",");

                if(components[3].equals("EW")&& components[2].equals("Clothing")){
                    for(Payment tem: getPaymentObject()){
                        if(tem instanceof EWallet){
                            int sdt=((EWallet)tem).getDT();
                            if(Integer.valueOf(components[4])==sdt){
                                for(IDCard idc: idcm.getIDCards()){
                                    if(sdt==idc.getSDT()){
                                        String gioitinh=idc.getGioiTinh();
                                        String[] ngat= idc.ngaysinh.split("/");
                                        int namsinh=Integer.valueOf(ngat[2]);
                                        int tuoi= 2023-namsinh;
                                        if((gioitinh.equals("Female")&& tuoi<18)||(gioitinh.equals("Male")&&tuoi<20)){
                                            Double tien=Double.valueOf(components[1]);
                                            if(tien>500){
                                                ((EWallet)tem).pay(tien-tien*0.15);
                                            }
                                        }
                                        else{
                                            ((EWallet)tem).pay(Double.valueOf(components[1]));
                                        }
                                    }
                                    
                                }
                            }
                        }
                    }
                }
                else{
                    if(components[3].equals("EW")){
                        for(Payment tem: getPaymentObject()){
                            if(tem instanceof EWallet){
                                int sdt=((EWallet)tem).getDT();
                                if(Integer.valueOf(components[4])==sdt){
                                    ((EWallet)tem).pay(Double.valueOf(components[1]));
                                }
                            }
                        }
                    }
                    if(components[3].equals("BA")){
                        for(Payment tem: getPaymentObject()){
                            if(tem instanceof BankAccount){
                                int sdd=((BankAccount)tem).getSTK();
                                if(Integer.valueOf(components[4])==sdd)
                                    ((BankAccount)tem).pay(Double.valueOf(components[1]));
                            }
                        }
                    }
                    if(components[3].equals("CC")){
                        for(Payment tem: getPaymentObject()){
                            if(tem instanceof ConvenientCard){
                                int sdd=((ConvenientCard)tem).getDinhDanh();
                                if(Integer.valueOf(components[4])==sdd)
                                    ((ConvenientCard)tem).pay(Double.valueOf(components[1]));
                            }
                        }
                    } 
                } 
            }
            sc.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
