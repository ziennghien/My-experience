public class Rating {
    private int maUser;
    private int maPhim;
    private int point;
    private long dateRv;
    public Rating( int maUser, int maPhim, int point, long dateRv){
        this.maUser=maUser;
        this.maPhim=maPhim;
        this.point=point;
        this.dateRv=dateRv;
    }
    public int getMaUser(){
        return this.maUser;
    }
    public void setMaUser(int ma){
        this.maUser=ma;
    }
    public int getMaPhim(){
        return this.maPhim;
    }
    public void setMaPhim(int ma){
        this.maPhim=ma;
    }
    public int getPoint(){
        return this.point;
    }
    public void setPoint(int point){
        this.point=point;
    }
    public long getDateRv(){
        return this.dateRv;
    }
    public void setDateRv(long date){
        this.dateRv=date;
    }

    @Override
    public String toString(){
        return "Rating["+this.maUser+","+this.maPhim+","+this.point+","+this.dateRv+"]";
    }
}
