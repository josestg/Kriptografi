#include <stdio.h>
#include <string.h>

void help(char *argv[]){
    printf("Encrypt :  %s E plain.txt cipher.txt \n", argv[0]);
    printf("Decrypt :  %s D cipher.txt plain.txt \n", argv[0]);
}


int main(int argc, char *argv[]){
    FILE *fin,*fout;
    char p,c, K[100];
    int i,n;

    if(argc<4){
        help(argv);
        return 0;
    }

    fin = fopen(argv[2],"rb");
    fout = fopen(argv[3],"wb");
    if(fin == NULL)
        printf ("Kesalahan dalam membuka %s sebagai berkas masukan",argv[2]);

    if(argv[1][0]=='E')
        printf("Enkripsi %s menjadi %s ...\n\n", argv[2],argv[3]);
    else if(argv[1][0]=='D')
        printf("Dekripsi %s menjadi %s ...\n\n", argv[2],argv[3]);
    else{
        help(argv);
        return 0;
    }
    
    printf("Kata kunci : "); gets(K);

    n = strlen(K);
    i = 0;
    while((p = getc(fin))!=EOF){
        c = p^K[i]; //XOR Operation
        putc(c,fout);
        i++;
        if(i>(n-1)) i = 0;
    }

    fclose(fin);
    fclose(fout);
}