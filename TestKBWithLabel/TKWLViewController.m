//
//  TKWLViewController.m
//  TestKBWithLabel
//
//  Created by Anthony Kong on 7/03/2014.
//  Copyright (c) 2014 Anthony Kong. All rights reserved.
//

#import "TKWLViewController.h"
#import "TKWLCell.h"

@interface TKWLViewController ()

@end

@implementation TKWLViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView {
    return 1;
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    return 5;
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    static NSString *CellIdentifier = @"Cell";
    
    TKWLCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    if (cell == nil) {
        cell = [[TKWLCell alloc] initWithStyle:UITableViewCellStyleSubtitle
                               reuseIdentifier:CellIdentifier];
    }
    
    UITextField *tf = [[UITextField alloc] initWithFrame:CGRectMake(0, 0, 0, 0)];
    [tf setKeyboardType:UIKeyboardTypeNumberPad];
    [cell.lblTest addSubview:tf];
    [cell.lblTest setUserInteractionEnabled:YES];

    
    cell.accessoryType = UITableViewCellAccessoryDetailDisclosureButton;
    [cell.lblTest setText:[NSString stringWithFormat:@"cell %d", indexPath.row]];

    return cell;
}

@end
