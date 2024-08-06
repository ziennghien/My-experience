public class ConvenientCard implements Payment{
    private String type;
	private IDCard idc;
	private double sodu;
	public String getType() throws CannotCreateCard {
		String[] ngat= idc.ngaysinh.split("/");
		int namsinh=Integer.valueOf(ngat[2]);
		if(namsinh<2005){
			this.type="Adult";
			return this.type;
		}
		else if(namsinh<=2011&&namsinh>=2005){
			this.type="Student";
			return this.type;
		}
		else
			throw new CannotCreateCard("Not enough age");
	}
	public int getDinhDanh(){
		return this.idc.getSoDinhDanh();
	}
	public ConvenientCard(IDCard idc)throws CannotCreateCard{
		this.idc=idc;
		this.sodu=100;
		this.type=getType();
	}
	public boolean pay(double amount){
		double thanhtoan=0;
		if(this.type.equals("Student")){
			thanhtoan=amount;
		}
		if(this.type.equals("Adult")){
			thanhtoan=amount+amount*0.01;
		}
		if(thanhtoan<=this.sodu){
			this.sodu=this.sodu-thanhtoan;
			return true;
		}
		else{
			return false;
		}
	}
	public double checkBalance(){
		return this.sodu;
	}
	public void topUp(double amount){
		this.sodu=this.sodu+amount;
	}
	@Override
	public String toString(){
			return this.idc+","+this.type+","+this.sodu;
	}
}
