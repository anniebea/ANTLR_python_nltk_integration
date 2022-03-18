*********

**Darba autore:** Anitra Adriāna Beināre

**Studentu apliecības Nr.:** ab19155

**Izstrādāts:** 03/2022

**Izstrādes vide:** JetBrains PyCharm Professional

*********

Projektā iekļautais kods ļauj lietotājam padot programmai teksta datni, 
no kura tiks veidots sintakes koks, atbilstoši **_Pam_v2_** gramatikai.
Programmas darbības laikā tiek izveidota koka struktūra sistēmas atmiņā un tā tiek pārveidota tā, 
lai to varētu attēlot lietotājam vizuālā formātā.  


*********

<h3>Lietotāja instrukcija iebūvētajai gramatikai Pam_v2</h3>

Nepieciešams nodrošināt ANTLR spraudni un šādas _Python_ pakotnes:
* pip
* nltk
* antlr4-python3-runtime

Lai uzsāktu programmu, komandrindā ar "cd" komandu jānavigē līdz šī projekta 
datņu mapei (automātiska darbība, ja izmanto _PyCharm_ iebūvēto termināli) un jāievada komanda `python main.py tests.txt`, 
kur "tests.txt" ir projekta datņu mapē ievietotās ievades datnes nosaukums (obligāti jāiekļauj ".txt"). 

Rezultātā programmas atmiņā tiks izveidots abstraktās sintakes koks, 
kurš tiks izvadīts kā zīmējums izlecošā logā. 

Ja padotajā datnē ir kļūdas (ievades dati neatbilst **_Pam_v2_** gramatikai), 
tiek izvadīts paziņojums konsolē, kurā uzsāk programmu.

*********

<h3>Uzstādīšanas nosacījumi jaunai gramatikai</h3>

Jaunas gramatikas uzstādīšanas soļi:
1) ievieto datni ar gramatikas definējumu (datnes tips - _.g4_) projekta datņu mapē;
2) izstrādes vidē ar labo peles klikšķi izvēlas gramatikas definējuma datni, izvēlas "_Configure ANTLR..._:
   1) ieraksta "**_Python3_**" valoda laukā "_Language_";
   2) Opcionāli - ievada nosaukumu datņu mapei, kurā izvadīs programmas darbībai nepieciešamos parsera failus, ievadot nosaukumu
   ievadlaukā "_Output directory where all output is generated_";
3) ar labo peles klikšķi izvēlas gramatikas definējuma datni, izvēlas "_Generate ANTLR Recognizer_";
4) pārbauda, ka tikko ģenerētā datņu mape satur datnes ar nosaukumiem "_LanguageLexer.py_" un "_LanguageParser.py_", 
   kur _Language_ ir gramatikas nosaukums;
5) `main.py` datnē:
   1) pārmaina 4. un 5. rindu kodu, izmantojot jaunās gramatikas datnes;
   2) pārmaina 14. rindas kodu, ievietojot "progr" vietā uzsākšanas komandu no gramatikas definējuma datnes.

*********

Piemērs izvadītam rezultātam:
![img.png](img.png)

Sistēmas atmiņā piemēra koks tiek uzglabāts `String` formātā, formatēti struktūra ir šāda:

<pre>
(progr
   (series 
      (stmt 
         (loop while 
            (log_expr 
               (log_term 
                  (log_elem true)
               )
            ) 
         do 
            (series 
               (stmt 
                  (cond_stmt if 
                     (log_expr 
                        (log_term 
                           (log_elem 
                              (condition 
                                 (pos_condition 
                                    (expr 
                                       (term 
                                          (elem x)
                                       )
                                    )
                                 = 
                                    (expr 
                                       (term 
                                          (elem true)
                                       )
                                    )
                                 )
                              )
                           )
                        and 
                           (log_elem 
                              (condition 
                                 (neg_condition not 
                                    (pos_condition 
                                       (expr 
                                          (term 
                                             (elem y)
                                          )
                                       ) 
                                    = 
                                       (expr 
                                          (term 
                                             (elem false)
                                          )
                                       )
                                    )  
                                 )
                              )
                           )
                        )
                     ) 
                  then 
                     (series 
                        (stmt 
                           (assign_stmt z := 
                              (expr 
                                 (term 
                                    (elem 1)
                                 * 
                                    (elem 2)
                                 ) 
                              + 
                                 (term 
                                    (elem 3)
                                 * 
                                    (elem 4)
                                 / 
                                    (elem 5)
                                 )
                              - 
                                 (term 
                                    (elem 1)
                                 )
                              )
                           )
                        )
                     ) 
                  else 
                     (series 
                        (stmt 
                           (assign_stmt y := 
                              (expr 
                                 (term 
                                    (elem false)
                                 )
                              )
                           )
                        )
                     ) 
                  fi)
               )
            ; 
               (stmt 
                  (cond_stmt if 
                     (log_expr 
                        (log_term 
                           (log_elem 
                              (condition 
                                 (pos_condition 
                                    (expr 
                                       (term 
                                          (elem x)
                                       )
                                    )
                                 = 
                                    (expr 
                                       (term 
                                          (elem false)
                                       )
                                    )
                                 )
                              )
                           )
                        )
                     )
                  then 
                     (series 
                        (stmt 
                           (assign_stmt y := 
                              (expr 
                                 (term 
                                    (elem 8)
                                 )
                              )
                           )
                        )
                     )
                  else 
                     (series 
                        (stmt 
                           (assign_stmt x := 
                              (expr 
                                 (term 
                                    (elem false)
                                 )
                              )
                           )
                        )
                     ) 
                  fi)
               )
            ; 
               (stmt 
                  (cond_stmt if 
                     (log_expr 
                        (log_term 
                           (log_elem 
                              (condition 
                                 (pos_condition 
                                    (expr 
                                       (term 
                                          (elem x)
                                       )
                                    ) 
                                 < 
                                    (expr 
                                       (term 
                                          (elem 2)
                                       )
                                    )
                                 )
                              )  
                           )
                        )
                     )
                  then 
                     (series 
                        (stmt 
                           (cond_stmt if 
                              (log_expr 
                                 (log_term 
                                    (log_elem 
                                       (condition 
                                          (pos_condition 
                                             (expr 
                                                (term 
                                                   (elem x)
                                                )
                                             ) 
                                          < 
                                             (expr 
                                                (term 
                                                   (elem 2)
                                                )
                                             )
                                          )
                                       )
                                    )
                                 )
                              ) 
                           then 
                              (series 
                                 (stmt 
                                    (assign_stmt c := 
                                       (expr 
                                          (term 
                                             (elem 7)
                                          )
                                       )
                                    )
                                 )
                              ) 
                           else 
                              (series 
                                 (stmt 
                                    (assign_stmt x := 
                                       (expr 
                                          (term 
                                             (elem true)
                                          )
                                       )
                                    )
                                 )
                              ) 
                           fi)
                        )
                     ) 
                  else 
                     (series 
                        (stmt 
                           (assign_stmt x :=
                              (expr 
                                 (term    
                                    (elem true)
                                 )
                              )
                           )
                        )
                     ) 
                  fi)
               )
            )
         end)
      )
   )
)
</pre>