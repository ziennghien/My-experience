public class BankAccount implements Payment, Transfer{
    private int stk;
    private double lai;
    private double sodu;
    public BankAccount(int stk,double lai){
        this.stk=stk;
        this.lai=lai;
        this.sodu=50;
    }

    public int getSTK(){
        return this.stk;
    }
    public void topUp(double nap){
        this.sodu=this.sodu+nap;
    }
    public boolean pay(double amount){
		if(amount<=this.sodu-50){
			this.sodu=this.sodu-amount;
			return true;
		}
		else
			return false;
    }
    public double checkBalance(){
        return this.sodu;
    }
    
    public boolean transfer (double amount, Transfer to){
		double tienchuyen=amount+transferFee*amount;
		if(tienchuyen<=checkBalance()-50){
			if(to instanceof EWallet){
				((EWallet)to).topUp(amount);
			}
			if(to instanceof BankAccount){
				((BankAccount)to).topUp(amount);
			}
			this.sodu=this.sodu-tienchuyen;
			return true;
		}
		else{
			return false;
		}
	}
   
    @Override
    public String toString(){
        return this.stk+","+this.lai+","+this.sodu;
    }
}
