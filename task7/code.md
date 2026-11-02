## Problem Statement

Design a retail order dispatch and return analysis system to process incoming order quantities, dispatch records, and returned items. The program must calculate outstanding orders, update inventory counts, and detect inconsistent records where returned quantities exceed dispatched quantities or dispatches exceed orders.

---

## Algorithm

1. **Input Ingestion:** Accept initial inventory levels along with records for orders, dispatches, and returns for each product.
2. **Consistency Validation:** Check each product record to detect anomalies such as dispatches exceeding ordered quantities or returns exceeding dispatched quantities, logging any inconsistencies.
3. **Outstanding Order Calculation:** Determine outstanding order quantities by subtracting total dispatches from total orders.
4. **Inventory Update:** Adjust inventory levels by subtracting dispatches and adding returned items back to stock.
5. **Report Generation:** Return the updated inventory status, calculated outstanding orders, and any detected data inconsistencies.

---

## Flowchart

```mermaid
flowchart TD
    A[Start: Input Inventory, Orders, Dispatches, Returns] --> B[Initialize Results and Inconsistency Log]
    B --> C[Loop Through Each Product Record]
    C --> D{Are dispatches > orders or returns > dispatches?}
    D -- Yes --> E[Log Inconsistent Record Error] --> F
    D -- No --> F[Calculate Outstanding Orders]
    F --> G[Update Inventory: Subtract Dispatches & Add Returns]
    G --> H{More products to process?}
    H -- Yes --> C
    H -- No --> I[Return Analysis Report & Updated Inventory] --> J[End]

```

---



---

## Sample Input

```python
initial_inventory = {
    "Item_X": 100,
    "Item_Y": 50,
    "Item_Z": 200
}

order_records = {
    "Item_X": {"ordered": 40, "dispatched": 35, "returned": 5},
    "Item_Y": {"ordered": 20, "dispatched": 25, "returned": 2},
    "Item_Z": {"ordered": 60, "dispatched": 60, "returned": 0}
}

```

---

## Sample Output

```json
{
  "analysis": {
    "Item_X": {
      "outstanding_orders": 5,
      "updated_stock": 70
    },
    "Item_Z": {
      "outstanding_orders": 0,
      "updated_stock": 140
    }
  },
  "updated_inventory": {
    "Item_X": 70,
    "Item_Y": 50,
    "Item_Z": 140
  },
  "inconsistencies": [
    {
      "Item_Y": [
        "Dispatched quantity exceeds ordered quantity."
      ]
    }
  ]
}

```
