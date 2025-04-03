from cdm.base.staticdata.party.Party import Party
from cdm.base.staticdata.party.PartyRole import PartyRole
from cdm.event.common.BusinessEvent import BusinessEvent
from cdm.event.common.Trade import Trade
from cdm.event.common.TradeState import TradeState


def create_example_parties():
    buyer = Party(name="AJR Investments")
    seller = Party(name="Tradingfours Inc.")
    return buyer, seller


def create_example_trade():
    trade = Trade(
        tradeDate={"value": "2025-04-01"},
        product={"economicTerms": {}}
    )
    return trade


def setup_trade_parties(trade, buyer, seller):
    buyer_role = PartyRole(
        role="Buyer",
        partyReference={"globalReference": "party1"}
    )

    seller_role = PartyRole(
        role="Seller",
        partyReference={"globalReference": "party2"}
    )

    if not hasattr(trade, 'partyRole'):
        trade.partyRole = []
    trade.partyRole.append(buyer_role)
    trade.partyRole.append(seller_role)

    if not hasattr(trade, 'party'):
        trade.party = []
    trade.party.append(buyer)
    trade.party.append(seller)

    return trade


from cdm.event.common.State import State
from datetime import date


def create_business_event(trade):
    state_obj = State(
        closedState=None
    )

    trade_state = TradeState(
        trade=trade,
        state=state_obj,
        resetHistory=[],
        transferHistory=[],
        observationHistory=[],
        valuationHistory=[]
    )

    business_event = BusinessEvent(
        intent="ContractFormation",
        corporateActionIntent=None,
        eventDate=date(2025, 4, 2),
        effectiveDate=date(2025, 4, 2),
        packageInformation=None,
        instruction=[],
        eventQualifier=None,
        after=[]
    )

    business_event.after.append(trade_state)

    return business_event

if __name__ == "__main__":
    buyer, seller = create_example_parties()
    trade = create_example_trade()
    trade = setup_trade_parties(trade, buyer, seller)
    business_event = create_business_event(trade)

    # Print results
    print("Business Event created")
    print("\nBusiness Event Structure:")
    business_event_json = business_event.model_dump_json(indent=2)
    print(business_event_json)