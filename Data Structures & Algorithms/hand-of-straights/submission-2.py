class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        freq_map = {}
        hand.sort()

        for i in hand:
            freq_map[i] = freq_map.get(i, 0) + 1

        for card in hand:
            if freq_map[card] == 0:
                continue

            for next_card in range(card, card + groupSize):
                if not freq_map[next_card]:
                    return False
                
                freq_map[next_card] -= 1

        return True 
        