// 7.1 Deck of Cards: Design the data structures for a generic deck of cards.
//     Explain how you would subclass the data structures to implement Blackjack.

// The book specifies that it wants a standard 52-card set.

/* Let's begin by thinking about which attributes a card itself will have. 
   I can only come up with two: suit and value. That covers it.
   We will have 4 suits: Heart, Club, Diamond, Spade
   We will have 13 values within each suit.
*/

#include <iostream>
#include <stdlib.h>

class Card
{
public:
    enum Suit {Hearts, Diamonds, Clubs, Spades};
    enum Value {Ace, King, Queen, Jack, _10, _9, _8, _7, _6, _5, _4, _3, _2};

    Card();
    void setCard();
    void getCard();
    Suit getSuit();
    Value getValue();

private:
    Suit suit;
    Value value;
};

class Deck 
{
public: 
    Deck();
    void shuffle();
    void draw();
    bool card_in_deck(Card card, int index);

private: 
    Card cards[52];
    int number_drawn;
};

void Card::setCard()
{ /* *** ADD HERE */}

void Card::getCard()
{ /* *** ADD HERE */}

Card::Suit Card::getSuit()
{return suit;}

Card::Value Card::getValue()
{return value;}

bool Deck::card_in_deck(Card card, int index)
{
    bool match;
    for(int i=0; i<=index; i++)
    {
        if((card.getValue() == cards[i].getValue()) && (card.getSuit() == cards[i].getSuit()))
        {match = true; break;}
        else match = false;
    }
    return match;
}

Deck::Deck()
{
    Card card;
    bool match = false;
    for(int i=0; i<52; i++)
    {
        do{
            card.setCard();
            match = card_in_deck(card, i);
        }
        while (match == true);
        match = false;
        cards[i] = card;
    }
    
    number_drawn = 0;
}

void Deck::shuffle()
{
    Card card;
    bool match = false;
    for(int i=0; i<52; i++)
    {
        do{
            card.setCard();
            match = card_in_deck(card,i);
        }
        while(match == true);
        cards[i] = card;
    }

    number_drawn = 0;
}

void Deck::draw()
{
    cards[number_drawn].getCard();
    number_drawn++;
}

void create_cards()
{}

int main()
{
    create_cards();
}

