def select_latest_item(items):
    """Select the item with the latest date."""
    if not items:
        print("No items remaining after filtering.")
        return None
        
    selected_item = max(items, key=lambda item: item.datetime)
    print(f"Latest item: {selected_item.id} from {selected_item.datetime}")
    print(
        f"Choosing {selected_item.id} from {selected_item.datetime.date()}"
        + f" with {selected_item.properties['eo:cloud_cover']}% cloud cover"
    )
    
    # Print available assets
    max_key_length = len(max(selected_item.assets, key=len))
    for key, asset in selected_item.assets.items():
        print(f"{key.rjust(max_key_length)}: {asset.title}")
        
    return selected_item
