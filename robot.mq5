//+------------------------------------------------------------------+
//|                        TrendExpert.mq5                          |
//|            Copyright 2022, Kavram Demircan                       |
//|                    https://www.mql5.com                          |
//+------------------------------------------------------------------+
#property copyright "Copyright 2022, Kavram Demircan"
#property link      "https://www.mql5.com"
#property version   "3.3"

#include <Trade\Trade.mqh>  // Ticaret işlemleri için gerekli kütüphane

// Kullanıcı tarafından ayarlanabilir giriş parametreleri
input double Profit = 0.20;    // Pozisyon başına 20 cent kar hedefi.
input double StopLoss = 0.06;  // Kar/Zarar oranına göre 6 cent zarar durdurma.
input int maximumpositions = 1000;  // Açılabilecek maksimum pozisyon sayısı
input double max_margin_percentage = 20.0; // Serbest marjinin %20'si kullanılacak
input ENUM_TIMEFRAMES InputTimeframe = PERIOD_H1; // Kullanılacak zaman dilimi

CTrade trade;  // Ticaret işlemleri için nesne oluşturma

//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
  {
   CloseWhenProfit();   // Başlangıçta kârlı pozisyonları kapat
   OpenPositions();     // Yeni pozisyonlar aç
   return(INIT_SUCCEEDED); 
  }

//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
  {
   if(AccountInfoDouble(ACCOUNT_MARGIN_FREE) > 0)  // Serbest marjin varsa
     {
      OpenPositions();   // Yeni pozisyonlar aç
     }
   
   CloseWhenProfit();   // Kârlı pozisyonları kontrol et ve kapat
  }

//+------------------------------------------------------------------+
//| Pozisyon Kapatma Fonksiyonu                                      |
//+------------------------------------------------------------------+
void CloseWhenProfit()
  {
   for(int i=0; i<PositionsTotal(); i++)  // Tüm açık pozisyonları döngüyle kontrol et
     {
      ulong ticket = PositionGetTicket(i);  // Pozisyon biletini al
      PositionSelectByTicket(ticket);       // Pozisyonu seç
      double profit = PositionGetDouble(POSITION_PROFIT);  // Pozisyonun kârını al

      // Pozisyon kârı 20 cent'i aştığında kapatılır.
      if(profit >= Profit)
        {
         trade.PositionClose(ticket);  // Pozisyonu kapat
        }
     }
  }

//+------------------------------------------------------------------+
//| Pozisyon Açma Fonksiyonu                                         |
//+------------------------------------------------------------------+
void OpenPositions()
  {
   if(PositionsTotal() < maximumpositions)  // Maksimum pozisyon sayısına ulaşılmadıysa
     {
      double free_margin = AccountInfoDouble(ACCOUNT_MARGIN_FREE);  // Mevcut serbest marjin
      double max_usable_margin = (max_margin_percentage / 100.0) * free_margin; // Kullanılabilir maksimum marjin
      double lot_size = max_usable_margin / MarketInfo(Symbol(), MODE_MARGINREQUIRED);  // Lot miktarını ayarla

      // Lot miktarı minimum lotu aşmalı ve toplam marjinin %50'sinden fazlasını riske atmamalı
      if(lot_size >= SymbolInfoDouble(Symbol(), SYMBOL_VOLUME_MIN) && 
         (lot_size * MarketInfo(Symbol(), MODE_MARGINREQUIRED)) <= (free_margin * 0.5))
        {
         for(int i=0; i<SymbolsTotal(true); i++)  // Tüm sembolleri döngüyle kontrol et
           {
            string symbolname = SymbolName(i,true);  // Sembol adını al

            MqlRates PriceInfo[];  // Fiyat bilgisi için dizi oluştur
            ArraySetAsSeries(PriceInfo,true);  // Diziyi ters sırala (en son veri başta)
            int priceData = CopyRates(symbolname,InputTimeframe,0,6,PriceInfo);  // Son 6 periyotluk veriyi al

            // Eğer son kapanış fiyatı açılış fiyatından büyükse:
            if(PriceInfo[0].close > PriceInfo[0].open)
              {
               if(PositionsTotal() < maximumpositions)  // Tekrar maksimum pozisyon kontrolü
                 {
                  double ask = NormalizeDouble(SymbolInfoDouble(symbolname,SYMBOL_ASK),_Digits);  // Alış fiyatını al
                  double sl = ask - StopLoss;  // Zarar durdur seviyesi 6 cent altında.
                  double tp = ask + Profit;    // Kâr alma seviyesi 20 cent üzerinde.

                  // Pozisyonu açarken kâr ve zarar limitleri belirleniyor.
                  trade.Buy(lot_size, symbolname, ask, sl, tp, NULL);  // Alış pozisyonu aç
                 }
              }
           }
        }
     }
  }
//+------------------------------------------------------------------+
