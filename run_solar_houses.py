#!/usr/bin/env python3
"""
Simple runner for Solar Houses Detection System
"""

import os
import sys
from solar_houses_detector import SolarHousesDetector

def main():
    print("🏠 Solar Houses Detection System")
    print("=" * 40)
    print("This system focuses on finding houses with existing solar panels")
    print("and generates property data with high-resolution house images.")
    print()
    
    # Get API key from user
    api_key = input("Enter your Google Maps API key: ").strip()
    
    if not api_key:
        print("❌ No API key provided. Exiting.")
        return
    
    # Get location from user
    location = input("Enter location (e.g., 'St. Tammany Parish, LA', 'New Orleans, LA', 'Baton Rouge, LA'): ").strip()
    if not location:
        location = "St. Tammany Parish, LA"
    
    # Get number of properties to process
    try:
        max_properties = int(input("Number of properties to process (default 20): ") or "20")
    except ValueError:
        max_properties = 20
    
    print(f"\n🚀 Starting Solar Houses Detection with {max_properties} properties in {location}...")
    print("This will:")
    print(f"  • Generate realistic property data for {location}")
    print("  • Focus on houses with existing solar panels")
    print("  • Download high-resolution house images")
    print("  • Calculate solar potential and financial analysis")
    print("  • Generate CSV files with owner names, addresses, and images")
    print()
    
    # Initialize system
    system = SolarHousesDetector(api_key)
    
    try:
        # Run detection pipeline
        results_df = system.process_properties(max_properties, location)
        
        if not results_df.empty:
            # Print summary
            total_properties = len(results_df)
            properties_with_solar = results_df['has_solar_panels'].sum()
            properties_with_images = results_df['image_downloaded'].sum()
            avg_potential = results_df['solar_potential_score'].mean()
            
            print("\n" + "="*40)
            print("🎉 SOLAR HOUSES DETECTION COMPLETE")
            print("="*40)
            print(f"Properties Processed: {total_properties}")
            print(f"Properties with Solar Panels: {properties_with_solar}")
            print(f"Properties with Downloaded Images: {properties_with_images}")
            print(f"Average Solar Potential: {avg_potential:.1f}/100")
            print(f"Output Directory: {system.output_dir}")
            
            # Show solar properties
            solar_properties = results_df[results_df['has_solar_panels'] == True]
            if not solar_properties.empty:
                print(f"\n🏠 Properties with Solar Panels ({len(solar_properties)}):")
                for _, row in solar_properties.iterrows():
                    print(f"  • {row['property_id']}: {row['system_size_kw']} kW, "
                          f"{row['estimated_panel_count']} panels, "
                          f"${row['estimated_savings_annual']:,} annual savings")
            
            # Show high-potential properties
            high_potential = results_df[(results_df['has_solar_panels'] == False) & 
                                      (results_df['solar_potential_score'] > 70)]
            if not high_potential.empty:
                print(f"\n🌟 High Solar Potential Properties ({len(high_potential)}):")
                for _, row in high_potential.iterrows():
                    print(f"  • {row['property_id']}: {row['solar_potential_score']}/100 potential, "
                          f"{row['recommended_system_size_kw']} kW recommended, "
                          f"{row['roi_percentage']}% ROI")
            
            print(f"\n📁 Generated Files:")
            print(f"  • CSV Data: {system.output_dir}/data/solar_houses_summary.csv")
            print(f"  • House Images: {system.output_dir}/house_images/")
            print(f"  • Interactive Map: {system.output_dir}/interactive_map.html")
            print(f"  • Report: {system.output_dir}/reports/solar_houses_report.md")
            
            print(f"\n✅ Ready for solar detection model!")
            print(f"The CSV file contains owner names, addresses, and house images")
            print(f"focused on properties with existing solar panels.")
        else:
            print("❌ No properties were successfully processed")
            print("Please check your API key and try again.")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please check your API key and ensure Maps Static API is enabled.")

if __name__ == "__main__":
    main()
