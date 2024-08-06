public class EWallet implements Payment, Transfer {
	private int sdt;
	private double sodu;
	public EWallet(int sdt){
		this.sdt=sdt;
		this.sodu=0;
	}
	public int getDT(){
		return this.sdt;
	}
	public void topUp(double nap){
		this.sodu=this.sodu+nap;
	}
	public boolean transfer (double amount, Transfer to){
		double tienchuyen=amount+transferFee*amount;
		if(tienchuyen<=checkBalance()){
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
	
	public double checkBalance(){
		return this.sodu;
	}
	public boolean pay(double amount){
		if(amount<=this.sodu){
			this.sodu=this.sodu-amount;
			return true;
		}
		else
			return false;
	}
	
	@Override
	public String toString(){
		return this.sdt+","+this.sodu;
	}
}
