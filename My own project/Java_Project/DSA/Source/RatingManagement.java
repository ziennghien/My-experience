import java.util.*;
import java.io.*;

public class RatingManagement {
    private ArrayList<Rating> ratings;
    private ArrayList<Movie> movies;
    private ArrayList<User> users;

    // @Requirement 1
    public RatingManagement(String moviePath, String ratingPath, String userPath) {
        this.movies = loadMovies(moviePath);
        this.users = loadUsers(userPath);
        this.ratings = loadEdgeList(ratingPath);
    }

    private ArrayList<Rating> loadEdgeList(String ratingPath) {
        ArrayList<Rating> rs= new ArrayList<Rating>();
        try {
            File f = new File(ratingPath);
            Scanner sc = new Scanner(f);
            String line=sc.nextLine();
            while (sc.hasNextLine()) {
                line = sc.nextLine();
                String[] components = line.split(",");
                rs.add(new Rating(Integer.parseInt(components[0]),Integer.parseInt(components[1]),Integer.parseInt(components[2]),Long.parseLong(components[3])));
            }
            sc.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return rs;
    }

    private ArrayList<Movie> loadMovies(String moviePath) {
        ArrayList<Movie> rs= new ArrayList<Movie>();
        try {
            File f = new File(moviePath);
            Scanner sc = new Scanner(f);
            String line=sc.nextLine();
            while (sc.hasNextLine()) {
                line = sc.nextLine();
                String[] components = line.split(",");
                String[] genre= components[2].split("-");
                ArrayList<String> genres= new ArrayList<String>();
                for(String x: genre){
                    genres.add(x);
                }
                rs.add(new Movie(Integer.parseInt(components[0]),components[1],genres));
            }
            sc.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return rs;
    }

    private ArrayList<User> loadUsers(String userPath) {
        ArrayList<User> rs= new ArrayList<User>();
        try {
            File f = new File(userPath);
            Scanner sc = new Scanner(f);
            String line=sc.nextLine();
            while (sc.hasNextLine()) {
                line = sc.nextLine();
                String[] components = line.split(",");
                rs.add(new User(Integer.parseInt(components[0]), components[1], Integer.parseInt(components[2]),components[3] , components[4]));
            }
            sc.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return rs;
    }

    public ArrayList<Movie> getMovies() {
        return movies;
    }

    public ArrayList<User> getUsers() {
        return users;
    }

    public ArrayList<Rating> getRating() {
        return ratings;
    }

    // @Requirement 2
    public ArrayList<Movie> findMoviesByNameAndMatchRating(int userId, int rating) {
        ArrayList<Movie> rs= new ArrayList<Movie>();
        ArrayList<Integer> maphim= new ArrayList<Integer>();
        for(Rating r: ratings){
            if(r.getMaUser()==userId){
                if(r.getPoint()>=rating){
                    maphim.add(r.getMaPhim());
                }
            }
        }
        for(Movie m: movies){
            if(maphim.contains(m.getId())){
                rs.add(m);
            }
        }
        rs.sort(Comparator.comparing(Movie::getName));
        return rs; 
    }

    // Requirement 3
    public ArrayList<User> findUsersHavingSameRatingWithUser(int userId, int movieId) {
        ArrayList<User> rs= new ArrayList<User>();
        ArrayList<Integer> ma= new ArrayList<Integer>();
        int point=0;
        for(Rating r: ratings){
            if(r.getMaPhim()==movieId && r.getMaUser()==userId){
                point= r.getPoint();
                break;
            }
        }
        for(Rating r: ratings){
            if(r.getMaPhim()==movieId && r.getPoint()==point && r.getMaUser()!=userId){
                ma.add(r.getMaUser());
            }
        }
        for(User u: users){
            if(ma.contains(u.getId())){
                rs.add(u);
            }
        }
        return rs; 
    }

    // Requirement 4
    public ArrayList<String> findMoviesNameHavingSameReputation() {
        ArrayList<String> rs= new ArrayList<String>();
        int[] number= new int[movies.size()];
        for(Rating r: ratings){
            if(r.getPoint()>3){
                for(Movie m: movies){
                    if(m.getId()==r.getMaPhim()){
                        number[movies.indexOf(m)]++;
                    }
                }
            }
        }
        for(int i=0;i<number.length;i++){
            if(number[i]>=2){
                rs.add(movies.get(i).getName());
            }
        }
        /*Collections.sort(rs,new Comparator<String>() {
            @Override
            public int compare(String s1,String s2){
                return (s1.compareTo(s2));
            }
        });*/
        rs.sort(Comparator.naturalOrder());
        return rs; 
    }

    // @Requirement 5
    public ArrayList<String> findMoviesMatchOccupationAndGender(String occupation, String gender, int k,
            int rating) {
        ArrayList<String> rs= new ArrayList<String>();
        ArrayList<String> tenphim= new ArrayList<String>();
        ArrayList<Integer> mauser= new ArrayList<Integer>();
        ArrayList<Integer> maphim= new ArrayList<Integer>();
        for(User  u: users){
            if(u.getOccupation().equals(occupation)){
                if(u.getGender().equals(gender)){
                    mauser.add(u.getId());
                }
            }
        }
        for(Rating r: ratings){
            if(mauser.contains(r.getMaUser()) && r.getPoint()==rating){
                maphim.add(r.getMaPhim());
            }
        }
        for(Movie m: movies){
            if(maphim.contains(m.getId())){
                tenphim.add(m.getName());
            }
        }
        /*Collections.sort(tenphim,new Comparator<String>() {
            @Override
            public int compare(String s1,String s2){
                return (s1.compareTo(s2));
            }
        });*/
        tenphim.sort(Comparator.naturalOrder());
        for(int i=0; i<k;i++){
            rs.add(tenphim.get(i));
        }
        return rs; 
    }

    // @Requirement 6
    public ArrayList<String> findMoviesByOccupationAndLessThanRating(String occupation, int k, int rating) {
        ArrayList<String> rs= new ArrayList<String>();
        ArrayList<String> tenphim= new ArrayList<String>();
        ArrayList<Integer> mauser= new ArrayList<Integer>();
        ArrayList<Integer> maphim= new ArrayList<Integer>();
        for(User  u: users){
            if(u.getOccupation().equals(occupation)){
                mauser.add(u.getId());
            }
        }
        for(Rating r: ratings){
            if(mauser.contains(r.getMaUser()) && r.getPoint()<rating){
                maphim.add(r.getMaPhim());
            }
        }
        for(Movie m: movies){
            if(maphim.contains(m.getId())){
                tenphim.add(m.getName());
            }
        }
        tenphim.sort(Comparator.naturalOrder());
        for(int i=0; i<k;i++){
            rs.add(tenphim.get(i));
        }
        return rs; 
    }

    // @Requirement 7
    public ArrayList<String> findMoviesMatchLatestMovieOf(int userId, int rating, int k) {
        ArrayList<String> rs= new ArrayList<String>();
        ArrayList<String> tenphim= new ArrayList<String>();
        ArrayList<Integer> mauser= new ArrayList<Integer>();
        ArrayList<Integer> maphim= new ArrayList<Integer>();
        
        String gender=new String();
        for(User  u: users){
            if(u.getId()==userId){
                gender=u.getGender();
                break;
            }
        }
        long near=0;
        int newm=0;
        for(Rating r: ratings){
            if(r.getMaUser()==userId){
                if(r.getDateRv()>near&& r.getPoint()>=rating){
                    near=r.getDateRv();
                    newm = r.getMaPhim();
                }
            }
        }
        ArrayList<String> genres= new ArrayList<String>();
        for(Movie m: movies){
            if(m.getId()==newm){
                genres= new ArrayList<String>(m.getGenres());
            }
        }
        
        for(User u: users){
            if(u.getGender().equals(gender)){
                mauser.add(u.getId());
            }
        }
        for(Rating r:ratings){
            if(mauser.contains(r.getMaUser())){
                if(r.getPoint()>=rating){
                    maphim.add(r.getMaPhim());
                }
            }
        }
        for(Movie m: movies){
            if(maphim.contains(m.getId())){
                int flag=0;
                for(String a: genres){
                    if(m.getGenres().contains(a)){
                        flag=1;
                    }
                }
                if(flag!=0){
                    tenphim.add(m.getName());
                }
            }
        }
        tenphim.sort(Comparator.naturalOrder());
        for(int i=0; i<k;i++){
            rs.add(tenphim.get(i));
        }
        return rs; 
    }
}