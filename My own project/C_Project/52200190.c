#include <stdio.h>
#include <stdlib.h>
#include <string.h>
const float PI=3.1415926535;
void ghi_file(int bc,int bg,float nd){
    FILE *foutp;
    foutp= fopen("output.out","w");
    fprintf(foutp,"%d %d %0.3f",bc,bg,nd);
    fclose(foutp);
}
void Wind(int n,int dc,int dg,int ld,int bc,int bg,float nd,float nepc,float nepg);
void Rain(int n,int dc,int dg,int ld,int bc,int bg,float nd,float nepc,float nepg);
void Sun(int n,int dc,int dg,int ld,int bc,int bg,float nd,float nepc,float nepg);
void Fog(int n,int dc,int dg,int bc,int bg,float nd);
void Cloud(int n,int dc,int dg,int ld,int bc,int bg,float nd,float nepc,float nepg);
int main(){
    int n,dc,dg,ld,i,ss;
    char w[10];
    char weather[][6]={"Rain","Sun","Cloud","Fog","Wind"};
    int bc,bg;
    float nepc,nepg,nd;
    FILE *fin;
    fin= fopen("input.inp","r");
    fscanf(fin,"%d%d%d%d%s",&n,&dc,&dg,&ld,&w);
    fclose(fin);
    nepc=dc*dc;
    nepg=(dg*dg*PI)/4;
    if(n<0||n>1000||ld<1||ld>300){
        ghi_file(-1,-1,n);
    }
    else{
        for(i=0;i<5;i++){
            if(strcmp(w,weather[i])==0){
               break;
        }
    }
        switch(i){
        case 0:
            Rain(n,dc,dg,ld,bc,bg,nd,nepc,nepg);
            break;
        case 1:
            Sun(n,dc,dg,ld,bc,bg,nd,nepc,nepg);
            break;
        case 2:
            Cloud(n,dc,dg,ld,bc,bg,nd,nepc,nepg);
            break;
        case 3:
            Fog(n,dc,dg,bc,bg,nd);
            break;
        case 4:
            Wind(n,dc,dg,ld,bc,bg,nd,nepc,nepg);
            break;
        }
    }
 return 0;
}
void Wind(int n,int dc,int dg,int ld,int bc,int bg,float nd,float nepc,float nepg){
    int i,j;
    float min;
    if(dc<=0){
        dc=60;
    }
    if(dg<=0){
        dg=60;
    }
    bc=n/nepc;
    nd=n-bc*nepc;
    bg=nd/nepg;
    nd=nd-bg*nepg;
    if((bc+bg)>ld){
        if(nepg>nepc){
            bg=n/nepg;
            nd=n-bg*nepg;
            bc=nd/nepc;
            nd=nd-bc*nepc;
            if((bc+bg)>ld){
                for(j=0;j<=ld;j++){
                    i=ld-j;
                    min=n-j*nepg-i*nepc;
                    if(min>=0){
                        bc=i;
                        bg=j;
                        nd=min;
                    }
                }
            }
        }else{
           for(i=0;i<=ld;i++){
                i=ld-i;
                min=n-j*nepg-i*nepc;
                if(min>=0){
                    bc=i;
                    bg=j;
                    nd=min;
                }
            }
        }
    }
    ghi_file(bc,bg,nd);
}
void Rain(int n,int dc,int dg,int ld,int bc,int bg,float nd,float nepc,float nepg){
    int i,j,tem,plus;
    float min1,min2,nepdu;
    if(dc<=0){
        dc=60;
    }
    if(dg<=0){
        dg=60;
    }
    min1=n;
    bc=n/(nepc+nepg);
    nd=n-bc*(nepc+nepg);
    bg=bc;
    nepdu=nd;
    if(nd>=nepg&&nd>=nepc){
        if(nepc>nepg){
            plus=nd/nepc;
            bc=bc+plus;
            nd=nd-plus*nepc;
        }
        else{
            plus=nd/nepg;
            bg=bg+plus;
            nd=nd-plus*nepg;
        }
    }
    if(nd>=nepg&&nd<=nepc){
        plus=nd/nepg;
        bg=bg+plus;
        nd=nd-plus*nepg;
    }
    if(nd>=nepc&&nd<=nepg){
        plus=nd/nepc;
        bc=bc+plus;
        nd=nd-plus*nepc;
    }

    if((bc+bg)>ld){
        for(bc=0;bc<=(ld/2);bc++){
            nepdu=n-bc*(nepc+nepg);
            if(nepdu>=0){
                bg=bc;
                nd=nepdu;
            }
        }
        bc=bg;
        if((bc+bg)<ld){
            tem=ld-bc-bg;
            if(nd>=nepg&&nd>=nepc){
                if(nepc>nepg){
                    plus=nd/nepc;
                    if(plus>tem){
                        plus=tem;
                    }
                    bc=bc+plus;
                    nd=nd-plus*nepc;
                }
                else{
                    plus=nd/nepg;
                    if(plus>tem){
                        plus=tem;
                    }
                    bg=bg+plus;
                    nd=nd-plus*nepg;
                }
            }
            if(nd>=nepg&&nd<=nepc){
                plus=nd/nepg;
                if(plus>tem){
                    plus=tem;
                }
                bg=bg+plus;
                nd=nd-plus*nepg;
            }
            if(nd>=nepc&&nd<=nepg){
                plus=nd/nepc;
                if(plus>tem){
                    plus=tem;
                }
                bc=bc+plus;
                nd=nd-plus*nepc;
            }
        }
    }
    ghi_file(bc,bg,nd);
}
void Sun(int n,int dc,int dg,int ld,int bc,int bg,float nd,float nepc,float nepg){
    int i,j,S1,S2;
    int G,H,X,ss;
    if(dc<=0){
        dc=60;
    }
    if(dg<=0){
        dg=60;
    }
    G=dc%6;
    H=ld%5;
    if (G==H){
        X=5;
    }
    if (G-H==1){
        X=7;
    }
    if (G-H==2||G-H==-4){
        X=10;
    }
    if (G-H==3 || G-H==-3){
        X=12;
    }
    if (G-H==4 || G-H==-2){
        X=15;
    }
    if (G-H==5 ||G-H==-1){
        X=20;
    }
    n=n+n*((float)X/100);
    ld=ld-X;
    if(ld<=0){
        ld=0;
        bc=0;
        bg=0;
        nd=n;
        ghi_file(bc,bg,nd);
    }
    else{
        ss=(dc+dg)%3;
        switch(ss){
        case 0:
            Rain(n,dc,dg,ld,bc,bg,nd,nepc,nepg);
            break;
        case 1:
            Wind(n,dc,dg,ld,bc,bg,nd,nepc,nepg);
            break;
        case 2:
            Cloud(n,dc,dg,ld,bc,bg,nd,nepc,nepg);
            break;
        }
    }
}
void Fog(int n,int dc,int dg,int bc,int bg,float nd){
    bc=dc;
    bg=dg;
    nd=n;
    ghi_file(bc,bg,nd);
}
void Cloud(int n,int dc,int dg,int ld,int bc,int bg,float nd,float nepc,float nepg){
    int i,j,S1,S2;
    float min;
    if(dc<=0){
        dc=60;
    }
    if(dg<=0){
        dg=60;
    }
    S1=0;
    S2=0;
    for(i=1;i<n;i++){
        if(n%i==0){
             S1+=i;
        }
    }
    for(j=1;j<ld;j++){
        if(ld%j==0){
            S2+=j;
        }
    }
    if(n==S2&&ld==S1){
        bc=0;
        bg=0;
        nd=n;
    }
    else{
        bg=n/nepg;
        nd=n-bg*nepg;
        bc=nd/nepc;
        nd=nd-bc*nepc;
        if((bc+bg)>ld){
            if(nepc>nepg){
                bc=n/nepc;
                nd=n-bc+nepc;
                bg=nd/nepg;
                nd=nd-bc*nepc;
                if((bc+bg)>ld){
                        for(i=0;i<=ld;i++){
                            j=ld-i;
                            min=n-j*nepg-i*nepc;
                            if(min>=0){
                                bc=i;
                                bg=j;
                                nd=min;
                            }
                        }
                }
            }else{
                for(j=0;j<=ld;j++){
                    i=ld-j;
                    min=n-j*nepg-i*nepc;
                    if(min>=0){
                        bc=i;
                        bg=j;
                        nd=min;
                    }
                }
            }
        }
    }

    ghi_file(bc,bg,nd);
}

