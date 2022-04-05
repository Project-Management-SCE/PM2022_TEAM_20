#include <stdio.h>
#include <string.h>
#include <pcap/pcap.h>
#include <openssl/rc4.h>
#include<stdlib.h>

typedef unsigned char u8;
char err[PCAP_ERRBUF_SIZE];

static void PrintHex(char *s, u8 *buf, int len)
{
    printf("%s", s);
    for (int i = 0; i < len; ++i)
        printf("%02x ", buf[i]);
    printf("\n");
}

int main(int argc, char **argv)
{
    pcap_t *pcap = pcap_open_offline("wep.pcap", err);
    struct pcap_pkthdr header;
    const u8 *packet;
    u8 pack[2][8];
    int count=0;
    // <--- put the following lines in comment
    //packet = pcap_next(pcap, &header);
    //PrintHex("Message 1: ", packet, 20);
    //packet = pcap_next(pcap, &header);
    //PrintHex("Message 2: ", packet, 20);


    // --->
    u8 iv1[3],data1[4];
    u8 iv2[3],data2[4];
    // TODO: call pcap_next until you reach the first data package
    for(int i=0;i<20;i++){
        packet = pcap_next(pcap, &header);
        
        
        if(packet[0]==0x08){
            memcpy(pack[count],packet+24,8);
            count++;
        }
        if(count==2)
            break;
    }

    //PrintHex("first check-pack: ",pack[0],8);
    //PrintHex("second check pack: ",pack[1],8);
    //u8 secdata[8];
    //memcpy(secdata,pack[1],8);
    
    memcpy(iv1,pack[0],3);
    memcpy(data1,pack[0]+4,4);
    memcpy(iv2,pack[1],3);
    memcpy(data2,pack[1]+4,4);
    //PrintHex("iv1: \n",iv1,3);
    //PrintHex("data1: \n",data1,4);
    //PrintHex("iv2: \n",iv1,3);
    //PrintHex("data2: \n",data2,4);

    // TODO: copy the IV and the first 4 bytes of the data to local variables


    // TODO: search all the possible keys whose bytes are in the range 0x20..0x7f
    u8 ourkey[8];
    RC4_KEY* key;
    u8 temp[4];
    memcpy(ourkey,pack[0],3);
    u8 j,k,l,m,n;
    int break_flag=0;
    u8 secret_key[8];
    u8 secret_key2[8];
    int only_first_count=0;
    /*for (secret_key[3]='M'; secret_key[3]<=0x7f; ++secret_key[3])
    for (secret_key[4]='Y'; secret_key[4]<=0x7f; ++secret_key[4])
    for (secret_key[5]='K'; secret_key[5]<=0x7f; ++secret_key[5])
    for (secret_key[6]='E'; secret_key[6]<=0x7f; ++secret_key[6])
    for (secret_key[7]='Y'; secret_key[7]<=0x7f; ++secret_key[7])*/
    for (secret_key[3]=0x20; secret_key[3]<=0x7f; ++secret_key[3]){
        for (secret_key[4]=0x20; secret_key[4]<=0x7f; ++secret_key[4]){
            for (secret_key[5]=0x20; secret_key[5]<=0x7f; ++secret_key[5]){
                for (secret_key[6]=0x20; secret_key[6]<=0x7f; ++secret_key[6]){
                    for (secret_key[7]=0x20; secret_key[7]<=0x7f; ++secret_key[7]){
                        memcpy(secret_key,iv1,3);
                        memcpy(secret_key2,iv2,3);//copiing the iv of the second word we want to decript
                        memcpy(secret_key2+3,secret_key+3,5);
                        //PrintHex("check second key: \n",secret_key2,8);
                        //exit(1);
                        RC4_KEY key;
                        RC4_KEY key2;
                        RC4_set_key(&key,8,secret_key); //this function generates a secret key out of the seckret_key variable it got
                        u8 p[4];
                        RC4(&key,4,data1,p);

                        RC4_set_key(&key2,8,secret_key2);
                        u8 p2[4];
                        RC4(&key2,4,data2,p2);
                        //PrintHex("first key: ",secret_key,8);
                        //PrintHex("second key: ",secret_key2,8);
                        //exit(1);

                        //checking if both words were decripted correctly
                        if(memcmp(p,"\xaa\xaa\x03\x00",4)==0 && memcmp(p2,"\xaa\xaa\x03\x00",4)==0){
                            
                            printf("the correct key for both: \n");
                            PrintHex("the key: ",secret_key+3,5);
                            //exit(1);
                            
                            
            
                        }
                        else if(memcmp(p,"\xaa\xaa\x03\x00",4)==0 && memcmp(p2,"\xaa\xaa\x03\x00",4)!=0){
                            PrintHex("key only for data1: ",secret_key+3,5);
                            only_first_count++;
                        }
                        
                    }
                }
            }
        }
    }
    
    
    printf("number of keys that decript only the first data are: %d",only_first_count);
    
    
    
    /*for(j=0x20;j<=0x7f;j++)
        for(k=0x20;k<=0x7f;k++)
            for(l=0x20;l<=0x7f;l++)
                for(m=0x20;m<=0x7f;m++)
                    for(n=0x20;n<=0x7f;n++){
                        RC4_set_key(&key,8,ourkey);
                        memcpy(temp,ourkey+3,4);
                        RC4(&key,5,ourkey[3-7])
                    }
for (pack[3]=0x20; pack[3]<=0x7f; ++pack[3])
    for (pack[4]=0x20; pack[4]<=0x7f; ++pack[4])
        for()

    for (pack[3]='M'; pack[3]<=0x7f; ++pack[3]) //write MYKEY instead of 0X20:should be faster
    
    for (pack[4]='Y''; pack[4]<=0x7f; ++pack[4])
        
                for(pack[7])
                {
                    RC4_KEY key;
                    memcpy(pack,iv1,3);
    //              RC4_set_key(&key, 8, pack); 
                    u8 p[4];
    //              RC4(&key, 4, d, p);
                    if (memcmp(p,"\xaa\xaa\x03\x00") != 0)
                    {
                        continue;
                    }
                }

    */
    // TODO: for each 5-byte key K, perform two steps:
    // 
    //          -- step 1 --
    //          RC4_KEY key;
    //          RC4_set_key(&key, 8, secretKey); 
    //          where secretKey is an 8-byte key composed of the IV and K
    // 
    //          -- step 2 --
    //          u8 p[4];
    //          RC4(&key, 4, d, p);
    //          where d is a pointer to the first 4 bytes of the packet's data
    //          
    //          If after decryption you get the correct 4 bytes,
    //          try if K given the correct bytes on the second data packet.
    //          If so, print K.
}
