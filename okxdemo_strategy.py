from vnpy_novastrategy import (
    StrategyTemplate,
    BarData, TickData,
    TradeData, OrderData,
    ArrayManager, BarGenerator,
    Interval, datetime
)

class OkxDemoStrategy(StrategyTemplate):
    """DEMO strategy for OKX module"""

    author: str = "DEMO OKX"

    # parameters, can be set and changed in the strategy menu.
    trading_size: float = 0.01

    parameters: list = [
        "trading_size",
    ]

    # status variables, can be set and changed in the strategy menu.
    trading_pos: int = 0

    variables: list = [
        "trading_pos",
    ]

    def on_init(self) -> None:
        """Callback when strategy is inited"""
        # debug flag
        self.debug_trade_flag = False

        # the flag of this strategy is started or not.
        self.trade_start = False

        self.trading_symbol: str = self.vt_symbols[0]
        print(self.trading_symbol)
        print(self.trading_size)

        self.bar_dt: datetime = None
        self.bg: BarGenerator = BarGenerator(
            on_bar=lambda bar: None,
            window=1,
            on_window_bar=self.on_window_bar,
            interval=Interval.HOUR
        )
        self.am: ArrayManager = ArrayManager()
        self.load_bars(10, Interval.MINUTE)

        self.write_log("Strategy is inited.")

    def on_start(self) -> None:
        """Callback when strategy is started"""
        self.trade_start = True

        # when start again, set debug flag again
        self.debug_trade_flag = True

        self.write_log("Strategy is started.")

    def on_stop(self) -> None:
        """Callback when strategy is stoped"""
        self.trade_start = False

        # Cancel all existing orders
        self.cancel_all()
        
        self.write_log("Strategy is stopped.")

    def on_tick(self, tick: TickData) -> None:
        """Callback of tick data update"""
        # show tick data, strategy logic can process this tick data.
        print(tick)

        if self.trade_start:
            # below: just submit order to test.
            if self.debug_trade_flag:
                # submit trade order
                print("submit buy order:")
                buy_order = self.buy(self.trading_symbol, 50000.0, self.trading_size)
                print(buy_order)

                print("submit sell order:")
                sell_order = self.sell(self.trading_symbol, 150000.0, self.trading_size)
                print(sell_order)

                print("order submit!")
                self.debug_trade_flag = False
        
    def on_bars(self, bars: dict[str, BarData]) -> None:
        """Callback of 1-minute candle bars update"""
        pass

    def on_window_bar(self, bar: BarData) -> None:
        """Callback of window bar update"""
        pass

    def on_trade(self, trade: TradeData) -> None:
        """Callback of trade update"""
        self.trading_pos = self.get_pos(self.trading_symbol)
        self.put_event()

    def on_order(self, order: OrderData) -> None:
        """Callback of order update"""
        pass
