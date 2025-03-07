# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.async_support.base.exchange import Exchange
import hashlib
import math
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import ArgumentsRequired
from ccxt.base.errors import BadSymbol
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import NotSupported
from ccxt.base.errors import RateLimitExceeded
from ccxt.base.errors import ExchangeNotAvailable
from ccxt.base.errors import InvalidNonce
from ccxt.base.precise import Precise


class fcoin(Exchange):

    def describe(self):
        return self.deep_extend(super(fcoin, self).describe(), {
            'id': 'fcoin',
            'name': 'FCoin',
            'countries': ['CN'],
            'rateLimit': 2000,
            'userAgent': self.userAgents['chrome39'],
            'version': 'v2',
            'accounts': None,
            'accountsById': None,
            'hostname': 'fcoin.com',
            'has': {
                'cancelOrder': True,
                'CORS': False,
                'createOrder': True,
                'fetchBalance': True,
                'fetchClosedOrders': True,
                'fetchCurrencies': False,
                'fetchDepositAddress': False,
                'fetchMarkets': True,
                'fetchOHLCV': True,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchOrderBook': True,
                'fetchOrderBooks': False,
                'fetchOrders': True,
                'fetchTicker': True,
                'fetchTime': True,
                'fetchTrades': True,
                'fetchTradingLimits': False,
                'withdraw': False,
            },
            'timeframes': {
                '1m': 'M1',
                '3m': 'M3',
                '5m': 'M5',
                '15m': 'M15',
                '30m': 'M30',
                '1h': 'H1',
                '1d': 'D1',
                '1w': 'W1',
                '1M': 'MN',
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/42244210-c8c42e1e-7f1c-11e8-8710-a5fb63b165c4.jpg',
                'api': {
                    'public': 'https://api.{hostname}',
                    'private': 'https://api.{hostname}',
                    'market': 'https://api.{hostname}',
                    'openapi': 'https://www.{hostname}',
                },
                'www': 'https://www.fcoin.com',
                'referral': 'https://www.fcoin.com/i/Z5P7V',
                'doc': 'https://developer.fcoin.com',
                'fees': 'https://fcoinjp.zendesk.com/hc/en-us/articles/360018727371',
            },
            'api': {
                'openapi': {
                    'get': [
                        'symbols',
                    ],
                },
                'market': {
                    'get': [
                        'ticker/{symbol}',
                        'depth/{level}/{symbol}',
                        'trades/{symbol}',
                        'candles/{timeframe}/{symbol}',
                    ],
                },
                'public': {
                    'get': [
                        'symbols',
                        'currencies',
                        'server-time',
                    ],
                },
                'private': {
                    'get': [
                        'accounts/balance',
                        'assets/accounts/balance',
                        'broker/otc/suborders',
                        'broker/otc/suborders/{id}',
                        'broker/otc/suborders/{id}/payments',
                        'broker/otc/users',
                        'broker/otc/users/me/balances',
                        'broker/otc/users/me/balance',
                        'broker/leveraged_accounts/account',
                        'broker/leveraged_accounts',
                        'orders',
                        'orders/{order_id}',
                        'orders/{order_id}/match-results',  # check order result
                    ],
                    'post': [
                        'assets/accounts/assets-to-spot',
                        'accounts/spot-to-assets',
                        'broker/otc/assets/transfer/in',
                        'broker/otc/assets/transfer/out',
                        'broker/otc/suborders',
                        'broker/otc/suborders/{id}/pay_confirm',
                        'broker/otc/suborders/{id}/cancel',
                        'broker/leveraged/assets/transfer/in',
                        'broker/leveraged/assets/transfer/out',
                        'orders',
                        'orders/{order_id}/submit-cancel',  # cancel order
                    ],
                },
            },
            'fees': {
                'trading': {
                    'tierBased': False,
                    'percentage': True,
                    'maker': -0.0002,
                    'taker': 0.0003,
                },
            },
            'limits': {
                'amount': {'min': 0.01, 'max': 100000},
            },
            'options': {
                'createMarketBuyOrderRequiresPrice': True,
                'fetchMarketsMethod': 'fetch_markets_from_open_api',  # or 'fetch_markets_from_api'
                'limits': {
                    'BTM/USDT': {'amount': {'min': 0.1, 'max': 10000000}},
                    'ETC/USDT': {'amount': {'min': 0.001, 'max': 400000}},
                    'ETH/USDT': {'amount': {'min': 0.001, 'max': 10000}},
                    'LTC/USDT': {'amount': {'min': 0.001, 'max': 40000}},
                    'BCH/USDT': {'amount': {'min': 0.001, 'max': 5000}},
                    'BTC/USDT': {'amount': {'min': 0.001, 'max': 1000}},
                    'ICX/ETH': {'amount': {'min': 0.01, 'max': 3000000}},
                    'OMG/ETH': {'amount': {'min': 0.01, 'max': 500000}},
                    'FT/USDT': {'amount': {'min': 1, 'max': 10000000}},
                    'ZIL/ETH': {'amount': {'min': 1, 'max': 10000000}},
                    'ZIP/ETH': {'amount': {'min': 1, 'max': 10000000}},
                    'FT/BTC': {'amount': {'min': 1, 'max': 10000000}},
                    'FT/ETH': {'amount': {'min': 1, 'max': 10000000}},
                },
            },
            'exceptions': {
                '400': NotSupported,  # Bad Request
                '401': AuthenticationError,
                '405': NotSupported,
                '429': RateLimitExceeded,  # Too Many Requests, exceed api request limit
                '1002': ExchangeNotAvailable,  # System busy
                '1016': InsufficientFunds,
                '2136': AuthenticationError,  # The API key is expired
                '3008': InvalidOrder,
                '6004': InvalidNonce,
                '6005': AuthenticationError,  # Illegal API Signature
                '40003': BadSymbol,
            },
            'commonCurrencies': {
                'DAG': 'DAGX',
                'PAI': 'PCHAIN',
                'MT': 'Mariana Token',
            },
        })

    async def fetch_markets(self, params={}):
        method = self.safe_string(self.options, 'fetchMarketsMethod', 'fetch_markets_from_open_api')
        return await getattr(self, method)(params)

    async def fetch_markets_from_open_api(self, params={}):
        # https://github.com/ccxt/ccxt/issues/5648
        response = await self.openapiGetSymbols(params)
        #
        #     {
        #         "status":"ok",
        #         "data":{
        #             "categories":["fone::coinforce", ...],
        #             "symbols":{
        #                 "mdaeth":{
        #                     "price_decimal":8,
        #                     "amount_decimal":2,
        #                     "base_currency":"mda",
        #                     "quote_currency":"eth",
        #                     "symbol":"mdaeth",
        #                     "category":"fone::bitangel",
        #                     "leveraged_multiple":null,
        #                     "tradeable":false,
        #                     "market_order_enabled":false,
        #                     "limit_amount_min":"1",
        #                     "limit_amount_max":"10000000",
        #                     "main_tag":"",
        #                     "daily_open_at":"",
        #                     "daily_close_at":""
        #                 },
        #             }
        #             "category_ref":{
        #                 "fone::coinforce":["btcusdt", ...],
        #             }
        #         }
        #     }
        #
        data = self.safe_value(response, 'data', {})
        markets = self.safe_value(data, 'symbols', {})
        keys = list(markets.keys())
        result = []
        for i in range(0, len(keys)):
            key = keys[i]
            market = markets[key]
            id = self.safe_string(market, 'symbol')
            baseId = self.safe_string(market, 'base_currency')
            quoteId = self.safe_string(market, 'quote_currency')
            base = self.safe_currency_code(baseId)
            quote = self.safe_currency_code(quoteId)
            symbol = base + '/' + quote
            precision = {
                'price': self.safe_integer(market, 'price_decimal'),
                'amount': self.safe_integer(market, 'amount_decimal'),
            }
            limits = {
                'amount': {
                    'min': self.safe_number(market, 'limit_amount_min'),
                    'max': self.safe_number(market, 'limit_amount_max'),
                },
                'price': {
                    'min': math.pow(10, -precision['price']),
                    'max': math.pow(10, precision['price']),
                },
                'cost': {
                    'min': None,
                    'max': None,
                },
            }
            active = self.safe_value(market, 'tradeable', False)
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'active': active,
                'precision': precision,
                'limits': limits,
                'info': market,
            })
        return result

    async def fetch_markets_from_api(self, params={}):
        response = await self.publicGetSymbols(params)
        #
        #     {
        #         "status":0,
        #         "data":[
        #             {
        #                 "name":"dapusdt",
        #                 "base_currency":"dap",
        #                 "quote_currency":"usdt",
        #                 "price_decimal":6,
        #                 "amount_decimal":2,
        #                 "tradable":true
        #             },
        #         ]
        #     }
        #
        result = []
        markets = self.safe_value(response, 'data')
        for i in range(0, len(markets)):
            market = markets[i]
            id = self.safe_string(market, 'name')
            baseId = self.safe_string(market, 'base_currency')
            quoteId = self.safe_string(market, 'quote_currency')
            base = self.safe_currency_code(baseId)
            quote = self.safe_currency_code(quoteId)
            symbol = base + '/' + quote
            precision = {
                'price': market['price_decimal'],
                'amount': market['amount_decimal'],
            }
            limits = {
                'price': {
                    'min': math.pow(10, -precision['price']),
                    'max': math.pow(10, precision['price']),
                },
            }
            active = self.safe_value(market, 'tradable', False)
            if symbol in self.options['limits']:
                limits = self.extend(self.options['limits'][symbol], limits)
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'active': active,
                'precision': precision,
                'limits': limits,
                'info': market,
            })
        return result

    async def fetch_balance(self, params={}):
        await self.load_markets()
        response = await self.privateGetAccountsBalance(params)
        result = {'info': response}
        balances = self.safe_value(response, 'data')
        for i in range(0, len(balances)):
            balance = balances[i]
            currencyId = self.safe_string(balance, 'currency')
            code = self.safe_currency_code(currencyId)
            account = self.account()
            account['free'] = self.safe_string(balance, 'available')
            account['total'] = self.safe_string(balance, 'balance')
            account['used'] = self.safe_string(balance, 'frozen')
            result[code] = account
        return self.parse_balance(result, False)

    def parse_bids_asks(self, orders, priceKey=0, amountKey=1):
        result = []
        length = len(orders)
        halfLength = int(length / 2)
        # += 2 in the for loop below won't transpile
        for i in range(0, halfLength):
            index = i * 2
            priceField = self.sum(index, priceKey)
            amountField = self.sum(index, amountKey)
            result.append([
                self.safe_number(orders, priceField),
                self.safe_number(orders, amountField),
            ])
        return result

    async def fetch_order_book(self, symbol=None, limit=None, params={}):
        await self.load_markets()
        if limit is not None:
            if (limit == 20) or (limit == 150):
                limit = 'L' + str(limit)
            else:
                raise ExchangeError(self.id + ' fetchOrderBook supports limit of 20 or 150. Other values are not accepted')
        else:
            limit = 'L20'
        request = {
            'symbol': self.market_id(symbol),
            'level': limit,  # L20, L150
        }
        response = await self.marketGetDepthLevelSymbol(self.extend(request, params))
        orderbook = self.safe_value(response, 'data')
        return self.parse_order_book(orderbook, orderbook['ts'], 'bids', 'asks', 0, 1)

    async def fetch_ticker(self, symbol, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
        }
        ticker = await self.marketGetTickerSymbol(self.extend(request, params))
        return self.parse_ticker(ticker['data'], market)

    def parse_ticker(self, ticker, market=None):
        timestamp = None
        symbol = None
        if market is None:
            tickerType = self.safe_string(ticker, 'type')
            if tickerType is not None:
                parts = tickerType.split('.')
                id = parts[1]
                symbol = self.safe_symbol(id, market)
        values = ticker['ticker']
        last = self.safe_number(values, 0)
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_number(values, 7),
            'low': self.safe_number(values, 8),
            'bid': self.safe_number(values, 2),
            'bidVolume': self.safe_number(values, 3),
            'ask': self.safe_number(values, 4),
            'askVolume': self.safe_number(values, 5),
            'vwap': None,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': self.safe_number(values, 9),
            'quoteVolume': self.safe_number(values, 10),
            'info': ticker,
        }

    def parse_trade(self, trade, market=None):
        symbol = None
        if market is not None:
            symbol = market['symbol']
        timestamp = self.safe_integer(trade, 'ts')
        side = self.safe_string_lower(trade, 'side')
        id = self.safe_string(trade, 'id')
        priceString = self.safe_string(trade, 'price')
        amountString = self.safe_string(trade, 'amount')
        price = self.parse_number(priceString)
        amount = self.parse_number(amountString)
        cost = self.parse_number(Precise.string_mul(priceString, amountString))
        fee = None
        return {
            'id': id,
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'type': None,
            'order': None,
            'side': side,
            'takerOrMaker': None,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': fee,
        }

    async def fetch_time(self, params={}):
        response = await self.publicGetServerTime(params)
        #
        #     {
        #         "status": 0,
        #         "data": 1523430502977
        #     }
        #
        return self.safe_integer(response, 'data')

    async def fetch_trades(self, symbol, since=None, limit=50, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
            'limit': limit,
        }
        if since is not None:
            request['timestamp'] = int(since / 1000)
        response = await self.marketGetTradesSymbol(self.extend(request, params))
        return self.parse_trades(response['data'], market, since, limit)

    async def create_order(self, symbol, type, side, amount, price=None, params={}):
        await self.load_markets()
        request = {
            'symbol': self.market_id(symbol),
            'side': side,
            'type': type,
        }
        # for market buy it requires the amount of quote currency to spend
        if (type == 'market') and (side == 'buy'):
            if self.options['createMarketBuyOrderRequiresPrice']:
                if price is None:
                    raise InvalidOrder(self.id + " createOrder() requires the price argument with market buy orders to calculate total order cost(amount to spend), where cost = amount * price. Supply a price argument to createOrder() call if you want the cost to be calculated for you from price and amount, or, alternatively, add .options['createMarketBuyOrderRequiresPrice'] = False to supply the cost in the amount argument(the exchange-specific behaviour)")
                else:
                    request['amount'] = self.cost_to_precision(symbol, amount * price)
            else:
                request['amount'] = self.cost_to_precision(symbol, amount)
        else:
            request['amount'] = self.amount_to_precision(symbol, amount)
        if (type == 'limit') or (type == 'ioc') or (type == 'fok'):
            request['price'] = self.price_to_precision(symbol, price)
        response = await self.privatePostOrders(self.extend(request, params))
        return {
            'info': response,
            'id': response['data'],
        }

    async def cancel_order(self, id, symbol=None, params={}):
        await self.load_markets()
        request = {
            'order_id': id,
        }
        response = await self.privatePostOrdersOrderIdSubmitCancel(self.extend(request, params))
        order = self.parse_order(response)
        return self.extend(order, {
            'id': id,
            'status': 'canceled',
        })

    def parse_order_status(self, status):
        statuses = {
            'submitted': 'open',
            'canceled': 'canceled',
            'partial_filled': 'open',
            'partial_canceled': 'canceled',
            'filled': 'closed',
            'pending_cancel': 'canceled',
        }
        return self.safe_string(statuses, status, status)

    def parse_order(self, order, market=None):
        #
        #     {
        #         "id": "string",
        #         "symbol": "string",
        #         "type": "limit",
        #         "side": "buy",
        #         "price": "string",
        #         "amount": "string",
        #         "state": "submitted",
        #         "executed_value": "string",
        #         "fill_fees": "string",
        #         "filled_amount": "string",
        #         "created_at": 0,
        #         "source": "web"
        #     }
        #
        id = self.safe_string(order, 'id')
        side = self.safe_string(order, 'side')
        status = self.parse_order_status(self.safe_string(order, 'state'))
        marketId = self.safe_string(order, 'symbol')
        market = self.safe_market(marketId, market)
        symbol = market['symbol']
        orderType = self.safe_string(order, 'type')
        timestamp = self.safe_integer(order, 'created_at')
        amount = self.safe_number(order, 'amount')
        filled = self.safe_number(order, 'filled_amount')
        price = self.safe_number(order, 'price')
        cost = self.safe_number(order, 'executed_value')
        feeCurrency = None
        feeCost = None
        feeRebate = self.safe_number(order, 'fees_income')
        if (feeRebate is not None) and (feeRebate > 0):
            if market is not None:
                feeCurrency = market['quote'] if (side == 'buy') else market['base']
            feeCost = -feeRebate
        else:
            feeCost = self.safe_number(order, 'fill_fees')
            if market is not None:
                feeCurrency = market['base'] if (side == 'buy') else market['quote']
        return self.safe_order({
            'info': order,
            'id': id,
            'clientOrderId': None,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': None,
            'symbol': symbol,
            'type': orderType,
            'timeInForce': None,
            'postOnly': None,
            'side': side,
            'price': price,
            'stopPrice': None,
            'cost': cost,
            'amount': amount,
            'remaining': None,
            'filled': filled,
            'average': None,
            'status': status,
            'fee': {
                'cost': feeCost,
                'currency': feeCurrency,
            },
            'trades': None,
        })

    async def fetch_order(self, id, symbol=None, params={}):
        await self.load_markets()
        request = {
            'order_id': id,
        }
        response = await self.privateGetOrdersOrderId(self.extend(request, params))
        return self.parse_order(response['data'])

    async def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        request = {'states': 'submitted,partial_filled'}
        return await self.fetch_orders(symbol, since, limit, self.extend(request, params))

    async def fetch_closed_orders(self, symbol=None, since=None, limit=None, params={}):
        request = {'states': 'partial_canceled,filled'}
        return await self.fetch_orders(symbol, since, limit, self.extend(request, params))

    async def fetch_orders(self, symbol=None, since=None, limit=None, params={}):
        if symbol is None:
            raise ArgumentsRequired(self.id + ' fetchOrders() requires a `symbol` argument')
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
            'states': 'submitted,partial_filled,partial_canceled,filled,canceled',
        }
        if limit is not None:
            request['limit'] = limit
        response = await self.privateGetOrders(self.extend(request, params))
        return self.parse_orders(response['data'], market, since, limit)

    def parse_ohlcv(self, ohlcv, market=None):
        return [
            self.safe_timestamp(ohlcv, 'id'),
            self.safe_number(ohlcv, 'open'),
            self.safe_number(ohlcv, 'high'),
            self.safe_number(ohlcv, 'low'),
            self.safe_number(ohlcv, 'close'),
            self.safe_number(ohlcv, 'base_vol'),
        ]

    async def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        if limit is None:
            limit = 20  # default is 20
        request = {
            'symbol': market['id'],
            'timeframe': self.timeframes[timeframe],
            'limit': limit,
        }
        if since is not None:
            sinceInSeconds = int(since / 1000)
            timerange = limit * self.parse_timeframe(timeframe)
            request['before'] = self.sum(sinceInSeconds, timerange) - 1
        response = await self.marketGetCandlesTimeframeSymbol(self.extend(request, params))
        data = self.safe_value(response, 'data', [])
        return self.parse_ohlcvs(data, market, timeframe, since, limit)

    def nonce(self):
        return self.milliseconds()

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        request = '/'
        openAPI = (api == 'openapi')
        privateAPI = (api == 'private')
        request += (api + '/') if openAPI else ''
        request += self.version + '/'
        request += '' if (privateAPI or openAPI) else (api + '/')
        request += self.implode_params(path, params)
        query = self.omit(params, self.extract_params(path))
        url = self.implode_params(self.urls['api'][api], {
            'hostname': self.hostname,
        })
        url += request
        if privateAPI:
            self.check_required_credentials()
            timestamp = str(self.nonce())
            query = self.keysort(query)
            if method == 'GET':
                if query:
                    url += '?' + self.rawencode(query)
            # HTTP_METHOD + HTTP_REQUEST_URI + TIMESTAMP + POST_BODY
            auth = method + url + timestamp
            if method == 'POST':
                if query:
                    body = self.json(query)
                    auth += self.urlencode(query)
            payload = self.string_to_base64(auth)
            signature = self.hmac(payload, self.encode(self.secret), hashlib.sha1, 'binary')
            signature = self.decode(self.string_to_base64(signature))
            headers = {
                'FC-ACCESS-KEY': self.apiKey,
                'FC-ACCESS-SIGNATURE': signature,
                'FC-ACCESS-TIMESTAMP': timestamp,
                'Content-Type': 'application/json',
            }
        else:
            if query:
                url += '?' + self.urlencode(query)
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, code, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if response is None:
            return  # fallback to default error handler
        status = self.safe_string(response, 'status')
        if status != '0' and status != 'ok':
            feedback = self.id + ' ' + body
            self.throw_exactly_matched_exception(self.exceptions, status, feedback)
            raise ExchangeError(feedback)
