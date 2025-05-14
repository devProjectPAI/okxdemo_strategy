# okxdemo_strategy
A demo strategy , used to test okx module : submit order, cancel order, get tickdata.


# how to install this stragety
This code is based on the /examples/sma_strategy/sma_strategy.py in the "https://github.com/veighna-global/vnpy_novastrategy".

All the stragety's logic has been removed, only add the debug test code for trade order submit and cancel process.

To install this stragety:

1. Find the path of package "vnpy_novastrategy" installed on your system.

   For example: /usr/local/lib/python3.10/dist-packages/vnpy_novastrategy/
   
   The stragety files will be in the : /usr/local/lib/python3.10/dist-packages/vnpy_novastrategy/strategies/

   
3. Copy the okxdemo_strategy.py into the directory of strategies.


# how to run this stragety
1. Use the example code in the README of "https://github.com/devProjectPAI/vnpy_okx".

This code will load NovaStrategyApp from package vnpy_novastrategy.


2. Prepare your okx api: apikey, secretkey, password.

   Suggest to use the okx "Demo trading" mode to create api.


3. Run the example code and click "Connect Gateway" in the Home Page.

   Need input okx api informations.


4. Open the Nova Strategy Menu to Add strategy of okxdemo_stragety.

   Need input the trade symbol.

   For example:

      SPOT trading vt_symbol: BTC-USDT.OKX

      or

      Leverage trading vt_symbol: BTC-USDT-SWAP.OKX (default: 3x, how to change this default leverage radio, need to be implemented at a later time)

   You can search the vt_symbol in the "Find Contract" Menu.



   Need input the trade_size.

      Default 0.01.  In this code, trade order will be sumbitted with a amount 0.01.


   Attention: this code uses a fixed price in the debug test trade order.

   The price is suitable for BTC:

       buy price: 50000.0

       sell price: 150000.0

   Obviously the trade order will not be filled with such price. That is easy for us to watch and check the order status on the OKX platform.

   If you want to use ETH-USDT.OKX to test, You need change the price to a suitable value for ETH.


6. After adding okxdemo_stragety, do init, start, stop :

   Initialize: init the stragety.

   Start: will set the flags. and stragety will submit trade order in the on_tick callback function. (You can check the orders on OKX platform after start)

   Stop: will set the flags. and stragety will cancel the trade orders.

   
