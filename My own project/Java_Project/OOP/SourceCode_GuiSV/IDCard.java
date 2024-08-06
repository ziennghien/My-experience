public class IDCard {
      protected int sodinhdanh;
      protected String ten;
      protected String gioitinh;
      protected String ngaysinh;
      protected String diachi;
      protected int sdt;
      public IDCard(int sodinhdanh,String ten, String gioitinh, String ngaysinh,String diachi,int sdt){
            this.sodinhdanh=sodinhdanh;
            this.ten=ten;
            this.gioitinh=gioitinh;
            this.ngaysinh=ngaysinh;
            this.diachi=diachi;
            this.sdt=sdt;
      }

      public void setSoDinhDanh(int sodinhdanh){
            this.sodinhdanh=sodinhdanh;
      }
      public int getSoDinhDanh(){
            return this.sodinhdanh;
      }
      public void setTen(String ten){
            this.ten=ten;
      }
      public String getTen(){
            return this.ten;
      }
      public void setGioiTinh(String gioitinh){
            this.gioitinh=gioitinh;
      }
      public String getGioiTinh(){
            return this.gioitinh;
      }
      public void SetNgaySinh(String ngaysinh){
            this.ngaysinh=ngaysinh;
      }
      public String getNgaySinh(){
            return this.ngaysinh;
      }
      public void SetDiaChi(String diachi){
            this.diachi=diachi;
      }
      public String getDiaChi(){
            return this.diachi;
      }
      public void setSDT(int sdt){
            this.sdt=sdt;
      }
      public int getSDT(){
            return this.sdt;
      }
      @Override
      public String toString(){
            return this.sodinhdanh+"," +this.ten+","+this.gioitinh+","+this.ngaysinh+","+this.diachi+","+this.sdt;
      }
}
